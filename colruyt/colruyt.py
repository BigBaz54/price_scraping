import base64
import time
import requests
import json


def get_all_store_ids():
    headers = {
        "accept": "*/*",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua": "Chromium;v=112, Not_A Brand;v=24, Opera GX;v=98",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site"
    }
    response = requests.get("https://ecgplacesmw.colruytgroup.com/ecgplacesmw/v3/fr/places/searchPlaces?ensignId=7&featureId=47&latitude=48.692054&longitude=6.184417&radius=50000", headers=headers)
    j = response.json()
    store_ids = []
    for store in j:
        store_ids.append(store["branchId"])
    return store_ids

def get_price(product_url, store_id=7426, proxy=None):
    session = requests.Session()
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "sec-ch-ua": "Chromium;v=112, Not_A Brand;v=24, Opera GX;v=98",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.6961.0 Safari/537.36"
    }
    if proxy:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        session.proxies = proxies
    session.headers = headers
    session.get("https://www.collectandgo.fr/cogofr/fr/accueil")
    session.get(f"https://www.collectandgo.fr/cogofr/fr/accueil/chooseCollectingPoint/{store_id}")
    response = session.get(product_url)
    html = response.text
    try:
        price64 = html.split('setPrice(')[1].split(',')[0]
        price = float(base64.b64decode(price64).decode("utf-8").replace(",", ".").strip())
        return price
    except:
        print("Request was blocked (proxies could be used to bypass this)")
        return None

if __name__ == "__main__":
    # print(get_all_store_ids())
    print(get_price("https://www.collectandgo.fr/cogofr/fr/detail_article/1822/GET_27_Liqueur_de_menthe_17_9__Bl_70cl"))
                    