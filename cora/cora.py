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
            price = document.querySelectorAll('div.c-product-detail__wrapper > div.c-product-detail__informations > div.c-product-detail__detail > div > div.c-price.c-product__price.c-price--xxlg > p > span:nth-child(1)')[0].innerText;
            return price;
        """
    )
    price = float(price.replace(',', '.').strip())
    return price

def switch_stores(driver, store_id):
    driver.delete_cookie('magasin_id')
    driver.add_cookie({'name': 'magasin_id', 'value': str(store_id)})
    driver.refresh()

def get_all_prices(driver, product_url, write_to_file=False):
    prices = []
    get_product_page(driver, product_url)
    for store_id in ([1]+list(range(70, 170))):
        switch_stores(driver, store_id)
        time.sleep(2)
        try:
            price = read_price(driver)
            prices.append(price)
            print(price)
        except:
            print('No price found')
    if write_to_file:
        with open(os.path.join('cora', f'prices_{product_url.split("/")[-1].split("-")[0]}.json'), 'w') as f:
            json.dump(prices, f)
    return prices

if __name__ == '__main__':
    driver = init_driver()
    prices = get_all_prices(driver, 'https://www.cora.fr/article/2781138/get-27-70cl-17-9-vol.html', write_to_file=True)
    print("Prices found: ", len(prices))
    print("Min price: ", min(prices))
    print("Average price: ", np.mean(prices))
    print("Standard deviation: ", np.std(prices))
