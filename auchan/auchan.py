import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
import numpy as np


def init_driver():
    driver = webdriver.Chrome()
    return driver

def get_product_page(driver, url):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'onetrust-reject-all-handler').click()

def read_price(driver):
    price = driver.execute_script(
        """
            price = document.querySelectorAll('div.offer-selector__add2cart-wrapper > section:nth-child(1) > div > .product-price')[0].innerText;
            return price;
        """
    )
    price = float(price.replace('€', '').replace(',', '.').strip())
    return price

def get_new_journey_id(driver):
    # asking server for a new journey id
    journey_id = driver.execute_script(
        """
            journey_id = await fetch("https://www.auchan.fr/journey/update", {
                "headers": {
                    "accept": "application/json",
                    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "content-type": "application/x-www-form-urlencoded",
                    "sec-ch-ua": "Not.A/Brand;v=8, Chromium;v=114, Google Chrome;v=114",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "x-requested-with": "XMLHttpRequest"
                },
                "referrer": "https://www.auchan.fr/get-27-liqueur-a-base-de-menthe-17-9/pr-C1586720",
                "referrerPolicy": "strict-origin-when-cross-origin",
                "body": "offeringContext.seller.id=ddfaf8fc-b37b-4e83-9bc1-d32f3566dccc&offeringContext.channels%5B0%5D=PICK_UP&offeringContext.storeReference=889&address.zipcode=54000&address.city=Nancy&address.country=France&location.latitude=48.69372222373215&location.longitude=6.183409641594068&accuracy=MUNICIPALITY&position=1&journeyId=defa0178-defa-defa-defa-defa01720217",
                "method": "POST",
                "mode": "cors",
                "credentials": "include"
                }).then((response) => response.json())
                .then((data) => (data['id']));
            return journey_id;
        """
    )
    return journey_id

def set_journey_id(driver, journey_id):
    driver.add_cookie({'name': 'lark-journey', 'value': journey_id})
    driver.refresh()
    
def switch_stores(driver, store_info, journey_id):
    request = f"""
        fetch("https://www.auchan.fr/journey/update",{{
            "headers": {{
                "accept": "application/json",
                "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                "content-type": "application/x-www-form-urlencoded",
                "sec-ch-ua": "Not.A/Brand;v=8, Chromium;v=114, Google Chrome;v=114",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-requested-with": "XMLHttpRequest"
            }},
            "referrer": "https://www.auchan.fr/get-27-liqueur-a-base-de-menthe-17-9/pr-C1586720",
            "referrerPolicy": "strict-origin-when-cross-origin",
            "body": "offeringContext.seller.id={store_info['seller_id']}&offeringContext.channels%5B0%5D={store_info['channels']}&offeringContext.storeReference={store_info['store_reference']}&journeyId={journey_id}",
            "method": "POST",
            "mode": "cors",
            "credentials": "include"
        }});"""
    driver.execute_script(request)
    driver.refresh()

def get_nearby_store_infos(latitude=48.99372222373215, longitude=6.283409641594068):
    headers = {
        "accept": "application/crest",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua": 'Not.A/Brand;v=8, Chromium;v=114, Google Chrome;v=114',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
        "x-crest-renderer": "journey-renderer",
        "x-requested-with": "XMLHttpRequest",
    }
    response = requests.get(f'https://www.auchan.fr/offering-contexts?address.zipcode=54000&location.latitude={latitude}&location.longitude={longitude}&accuracy=MUNICIPALITY&sellerType=GROCERY&channels=PICK_UP%2CSHIPPING', headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    forms = soup.find_all('form', class_='journey-offering-contexts__form journeyChoice')
    stores = []
    for form in forms:
        store = {}
        store['seller_id'] = form.find('input', attrs={'name': 'sellerId'}).get('value')
        store['channels'] = form.find('input', attrs={'name': 'channels'}).get('value')
        store['store_reference'] = form.find('input', attrs={'name': 'storeReference'}).get('value')
        stores.append(store)
    return stores

def get_french_cities_coordinates():
    with open(os.path.join('auchan', 'french_cities.json'), 'r') as f:
        data = json.load(f)
    return data

def get_all_store_infos(gps_coordinates, write_to_file=False):
    stores_ids = set()
    store_infos = []
    for coord in gps_coordinates:
        print("Looking for stores near: ", coord['city'])
        nearby_stores = get_nearby_store_infos(coord['lat'], coord['lng'])
        for store in nearby_stores:
            if store['seller_id'] not in stores_ids:
                stores_ids.add(store['seller_id'])
                print("New store found: ", store["seller_id"])
                store_infos.append(store)
                last_city_with_store = coord['city']
    if write_to_file:
        with open(os.path.join('auchan', 'store_infos.json'), 'w') as f:
            json.dump(store_infos, f)
    print("Last city with stores", last_city_with_store)
    return store_infos

def get_all_prices(driver, product_url, store_infos, write_to_file=False):
    prices = []
    get_product_page(driver, product_url)
    journey_id = get_new_journey_id(driver)
    set_journey_id(driver, journey_id)
    for store_info in store_infos:
        switch_stores(driver, store_info, journey_id)
        time.sleep(2)
        try:
            price = read_price(driver)
            prices.append(price)
            print(price)
        except:
            print('No price found')
    if write_to_file:
        with open(os.path.join('auchan', f'prices_{product_url.split(".fr/")[1].split("-")[0]}.json'), 'w') as f:
            json.dump(prices, f)
    return prices

if __name__ == '__main__':
    gps_coordinates = get_french_cities_coordinates()
    # store_infos = get_all_store_infos(gps_coordinates, write_to_file=True)
    with open(os.path.join('auchan', 'store_infos.json'), 'r') as f:
        store_infos = json.load(f)
    driver = init_driver()
    prices = get_all_prices(driver, 'https://www.auchan.fr/get-27-liqueur-a-base-de-menthe-17-9/pr-C1586720', store_infos, write_to_file=True)
    print("Prices found: ", len(prices))
    print("Min price: ", min(prices))
    print("Average price: ", np.mean(prices))
    print("Standard deviation: ", np.std(prices))
