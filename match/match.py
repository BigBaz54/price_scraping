import requests


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


if __name__ == '__main__':
    print(get_all_store_ids())