import os
import requests
import json
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def init_driver():
    driver = webdriver.Chrome()
    return driver

def get_all_store_ids(driver):
    # might be blocked by captcha
    driver.get("https://www.intermarche.com/produit/liqueur-menthe-179%C2%B0/7610113019214")
    time.sleep(10)
    store_ids = driver.execute_script(
        """
            store_ids = await fetch("https://www.intermarche.com/api/service/pdvs/v4/pdvs/zone?r=10000000&lat=48.649848&lon=6.185461&min=10", {
                "headers": {
                    "accept": "application/json, text/plain, */*",
                    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "isnode": "false",
                    "itm_code": "itm-code-node",
                    "sec-ch-device-memory": "8",
                    "sec-ch-ua": "Chromium;v=112, Not_A Brand;v=24, Opera GX;v=98",
                    "sec-ch-ua-arch": "x86",
                    "sec-ch-ua-full-version-list": "Chromium;v=112.0.5615.165, Not_A Brand;v=24.0.0.0, Opera GX;v=98.0.4759.82",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-model": "",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "x-itm-device-fp": "83259ec0-d4e1-46e5-b8fa-ac7b312a30cb",
                    "x-itm-session-id": "552cb211-e546-4609-bc29-d77efef6b405",
                    "x-pdv": "{ref:02155,isEcommerce:true,name:Super%20Jarville%20la%20Malgrange}",
                    "x-red-device": "red_fo_desktop",
                    "x-red-version": "3",
                    "x-service-name": "pdvs"
                },
                "referrer": "https://www.intermarche.com/produit/liqueur-menthe-179%C2%B0/7610113019214",
                "referrerPolicy": "strict-origin-when-cross-origin",
                "body": null,
                "method": "GET",
                "mode": "cors",
                "credentials": "include"
                })
                    .then((res) => res.json())
                    .then((j) => {
                        ids = [];
                        j.resultats
                            .forEach((r) => (ids.push(r.storeCode)));
                        return ids});
            return store_ids;
        """
    )
    return store_ids

def load_all_store_ids():
    with open(os.path.join('intermarche', 'store_ids.json'), 'r') as f:
        store_ids = json.load(f)
    return store_ids


if __name__ == '__main__':
    # prices = get_all_prices(write_to_file=True)
    # print("Prices found: ", len(prices))
    # print("Min price: ", min(prices))
    # print("Average price: ", np.mean(prices))
    # print("Standard deviation: ", np.std(prices))

    driver = init_driver()
    print(get_all_store_ids(driver))
    