import os
import time
import requests
import json
import numpy as np


def get_all_store_ids():
    headers = {
        "accept": "application/json",
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
    response = requests.get("https://api-drive.drive.supermarchesmatch.fr/sites_searches?bounds=40.60800042942077,-5.7989172982238113,53.0656190559823,9.907071595098811&position=40.886448635806275,-4.352994446661311", headers=headers)
    json = response.json()
    store_ids = []
    for store in json:
        store_ids.append(store['id'])
    return store_ids

def get_price(product_id=1704605, store_id=1):
    headers = {
        "accept": "application/json",
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
    data = {
        "moduleVersion":"drive",
        "sessionId":"83d260b4310bc15e4ffa6d6e86c3aa85",
        "region":"fr_FR",
        "pageId":2,
        "parameters":{
            "skus":[
                str(product_id)
            ]
        },
        "advanced":{
            "store":store_id,
            "device":"COMPUTER"
        }
    }
    response = requests.post("https://merch.drive.supermarchesmatch.fr/prd-smm-gXXhCuExuH2h8bF7Pajk/3.0/simplePageContent", headers=headers, json=data)
    price = list(response.json()['items'].items())[0][1]['price']
    return price

def get_all_prices(product_id=1704605, write_to_file=False):
    store_ids = get_all_store_ids()
    prices = []
    for store_id in store_ids:
        try:
            price = get_price(product_id, store_id)
            # it seems that a price of 999.99 means that the product is not available
            assert (price != 999.99)
            prices.append(price)
            print(price)
        except:
            print("No price found")
    if write_to_file:
        with open(os.path.join('match', 'prices.json'), 'w') as f:
            json.dump(prices, f)
    return prices

if __name__ == '__main__':
    prices = get_all_prices(write_to_file=True)
    print("Prices found: ", len(prices))
    print("Min price: ", min(prices))
    print("Average price: ", np.mean(prices))
    print("Standard deviation: ", np.std(prices))
    