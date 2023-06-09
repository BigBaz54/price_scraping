import requests


def get_valid_proxies():
    response = requests.get("https://free-proxy-list.net/")
    import pandas as pd
    proxy_list = pd.read_html(response.text)[0]
    proxy_list["url"] = "http://" + proxy_list["IP Address"] + ":" + proxy_list["Port"].astype(str)
    proxy_list.head()
    https_proxies = proxy_list[proxy_list["Https"] == "yes"]
    print(f"Found {len(https_proxies)} proxies")
          
    url = "https://httpbin.org/ip"
    good_proxies = []
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
    for proxy_url in https_proxies["url"]:
        proxies = {
            "http": proxy_url,
            "https": proxy_url,
        }
        
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=2)
            good_proxies.append(proxy_url)
            print(f"Proxy {proxy_url} OK, added to good_proxy list")
        except Exception:
            pass
    return good_proxies

def get_one_valid_proxy():
    response = requests.get("https://free-proxy-list.net/")
    import pandas as pd
    proxy_list = pd.read_html(response.text)[0]
    proxy_list["url"] = "http://" + proxy_list["IP Address"] + ":" + proxy_list["Port"].astype(str)
    proxy_list.head()
    https_proxies = proxy_list[proxy_list["Https"] == "yes"]
    print(f"Found {len(https_proxies)} proxies")
          
    url = "https://httpbin.org/ip"
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
    for proxy_url in https_proxies["url"]:
        proxies = {
            "http": proxy_url,
            "https": proxy_url,
        }
        
        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=2)
            print(f"Proxy {proxy_url} OK")
            return proxy_url
        except Exception:
            pass