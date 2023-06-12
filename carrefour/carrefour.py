import json
import os
import numpy as np
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
            price = document.querySelectorAll('#data-produit-card > div.main-details__pricing > div > div > div > div.pdp-pricing__block-left > div > div > span')[0].innerText;
            return price;
        """
    )
    price = float(price.replace(',', '.').replace('€', '').strip())
    return price

def switch_stores(driver, store_id):
    driver.delete_cookie('FRONTAL_STORE')
    driver.add_cookie({'name': 'FRONTAL_STORE', 'value': str(store_id)})
    driver.refresh()
    
def get_all_store_ids(driver, write_to_file=False):
    pass

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
    store_ids = get_all_store_ids(driver, write_to_file=True)
    with open(os.path.join('carrefour', 'store_ids.json'), 'r') as f:
        store_ids = json.load(f)
    prices = get_all_prices(driver, 'https://www.carrefour.fr/p/liqueur-get-27-7610113019214', store_ids, write_to_file=True)
    print("Prices found: ", len(prices))
    print("Min price: ", min(prices))
    print("Average price: ", np.mean(prices))
    print("Standard deviation: ", np.std(prices))
