import requests
from test_headers import test_headers

def get_carrefour(proxy=None):
    session = requests.Session()
    if proxy:
        proxies = {
            'http': proxy,
            'https': proxy
        }
        session.proxies = proxies
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "referer": "https://www.carrefour.fr/p/liqueur-get-27-7610113019214",
        "sec-ch-ua": '"Chromium";v="112", "Not_A Brand";v="24", "Opera GX";v="98"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 OPR/98.0.0.0",
        "x-requested-with": "XMLHttpRequest",
    }
    session.headers = headers
    response = session.get('https://www.cora.fr/article/2781138/get-27-70cl-17-9-vol.html')
    return response


if __name__ == '__main__':
    print(get_carrefour())