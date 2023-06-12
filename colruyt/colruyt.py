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
    response = requests.get("https://ecgplacesmw.colruytgroup.com/ecgplacesmw/v3/fr/places/searchPlaces?ensignId=7&featureId=47&latitude=0&longitude=0", headers=headers)
    j = response.json()
    store_ids = []
    for store in j:
        store_ids.append(store["placeId"])
    return store_ids


if __name__ == "__main__":
    print(get_all_store_ids())