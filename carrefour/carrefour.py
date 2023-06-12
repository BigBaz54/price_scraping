import json
import os
from bs4 import BeautifulSoup
import numpy as np
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def init_driver():
    driver = webdriver.Chrome()
    return driver

def get_product_page(driver, url):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

def read_price(driver):
    price = driver.execute_script(
        """
            prices = document.querySelectorAll('#data-produit-card > div.main-details__pricing > div > div > div > div.pdp-pricing__block-left > div > div > :last-child')[0].innerText;
            return prices;
        """
    )
    price = float(price.replace(',', '.').replace('€', '').strip())
    return price

def switch_stores(driver, store_id):
    driver.delete_cookie('FRONTAL_STORE')
    driver.add_cookie({'name': 'FRONTAL_STORE', 'value': str(store_id)})
    driver.refresh()

def get_all_store_ids(driver, write_to_file=False):
    store_ids = set()
    for page in range(1, 30):
        print(f'Page {page}')
        ids = driver.execute_script(
            f"""
                store_ids = await fetch("https://www.carrefour.fr/geoloc?lat=48.666668&lng=6.157199&postal_code=54600&city=Villers-L%C3%A8s-Nancy&address=30%20Rue%20Du%20Jardin%20Botanique&page={page}&limit=100&checkAvailability=true&modes%5B%5D=picking", {{
                    "headers": {{
                        "accept": "application/json, text/plain, */*",
                        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                        "sec-ch-ua": "Chromium;v=112, Not_A Brand;v=24, Opera GX;v=98",
                        "sec-ch-ua-mobile": "?0",
                        "sec-ch-ua-platform": "Windows",
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "x-requested-with": "XMLHttpRequest"
                    }},
                    "referrer": "https://www.carrefour.fr/p/liqueur-get-27-7610113019214",
                    "referrerPolicy": "strict-origin-when-cross-origin",
                    "body": null,
                    "method": "GET",
                    "mode": "cors",
                    "credentials": "include"
                }})
                    .then((res) => res.json())
                    .then((j) => {{
                        i = [];
                        j.data.stores.forEach(
                            (store) => i.push(store.ref)
                        );
                        console.log(i);
                        return i;
                    }});
                return store_ids;
            """
        ) or []
        for store_id in ids:
            if store_id not in store_ids:
                store_ids.add(store_id)
                print("New store id found: ", store_id)
    store_ids = list(store_ids)
    if write_to_file:
        with open(os.path.join('carrefour', 'store_ids.json'), 'w') as f:
            json.dump(store_ids, f)
    return store_ids

def get_all_prices(driver, product_url, store_ids, write_to_file=False):
    prices = []
    get_product_page(driver, product_url)
    for store_id in store_ids:
        switch_stores(driver, store_id)
        time.sleep(2)
        try:
            price = read_price(driver)
            prices.append(price)
            print(price)
        except:
            print('No price found')
    if write_to_file:
        with open(os.path.join('carrefour', f'prices_{product_url.split("/")[-1].split("-")[0]}.json'), 'w') as f:
            json.dump(prices, f)
    return prices


if __name__ == '__main__':
    driver = init_driver()
    # store_ids = get_all_store_ids(driver, write_to_file=True)
    with open(os.path.join('carrefour', 'store_ids.json'), 'r') as f:
        store_ids = json.load(f)
    prices = get_all_prices(driver, 'https://www.carrefour.fr/p/liqueur-get-27-7610113019214', store_ids, write_to_file=True)
    print("Prices found: ", len(prices))
    print("Min price: ", min(prices))
    print("Average price: ", np.mean(prices))
    print("Standard deviation: ", np.std(prices))
