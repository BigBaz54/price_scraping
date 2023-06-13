import requests
import numpy as np


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
    response = requests.get("https://storage.googleapis.com/assets.miam.tech/coursesu/config/prod/config.json", headers=headers)
    j = response.json()
    store_ids = j["available_stores"]
    return store_ids


if __name__ == "__main__":
    # store_ids = get_all_store_ids()
    # prices = get_all_prices("https://www.collectandgo.fr/cogofr/fr/detail_article/1822/GET_27_Liqueur_de_menthe_17_9__Bl_70cl", store_ids, proxies=True, write_to_file=True)
    # print("Prices found: ", len(prices))
    # print("Min price: ", min(prices))
    # print("Average price: ", np.mean(prices))
    # print("Standard deviation: ", np.std(prices))

    print(get_all_store_ids())
