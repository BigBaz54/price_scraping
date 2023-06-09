import requests
from bs4 import BeautifulSoup
from test_headers import test_headers


def get_carrefour_soup(store, proxy=None):
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
    
    session.cookies.set('TCID', '123642110344811350598')
    session.cookies.set('FRONTAL_STORE', store)
    session.cookies.set('pageCounterCrfOne', '35')
    session.cookies.set('tc_cj_v2', 'm_gGa**%22%27%20ZZZ%22**%22%27%20ZZZKPRPLOKNQJJMJZZZ%5D777%5Ecl_%5Dny%5B%5D%5D_mmZZZZZZKPRPLSPSMPOMNZZZ%5D')
    session.cookies.set('FRONTONE_SLOT', 'eyJjYXBhY2l0eU1heCI6NCwiY2FwYWNpdHlVc2VkIjoxLCJjdXRvZmYiOiIyMDIzLTA2LTA5VDEyOjAwOjAwKzAyOjAwIiwiZGF0ZUJlZ2luIjoiMjAyMy0wNi0wOVQxMzowMDowMCswMjowMCIsImRhdGVFbmQiOiIyMDIzLTA2LTA5VDE0OjAwOjAwKzAyOjAwIiwicmVmIjoiZjRiNmViZDctYjU2MS00MTdmLWE5MDAtODMyM2RmM2Q2MGFmIiwic3RhdHVzIjoiT1BFTiIsInRyYW5jaGUiOiIxQSIsImdyZWVuU2xvdCI6MH0%3D')
    session.cookies.set('OptanonAlertBoxClosed', '2023-06-08T19:10:44.857Z%3D')
    session.cookies.set('OneTrustGroupsConsent', '%2CC0048%2CC0001%2C')
    session.cookies.set('eupubconsent-v2', 'CPtFYzGPtFYzGAcABBENDHCgAAAAAAAAAChQAAAAAAAA.YAAAAAAAAAAA')
    session.cookies.set('OptanonConsent', 'isIABGlobal=false&datestamp=Fri+Jun+09+2023+10%3A41%3A13+GMT%2B0200+(heure+d%E2%80%99%C3%A9t%C3%A9+d%E2%80%99Europe+centrale)&version=6.12.0&hosts=&consentId=a89b317c-29ce-4070-842a-d9f4c26d2f87&interactionCount=1&landingPath=NotLandingPage&groups=C0048%3A1%2CC0001%3A1%2CC0040%3A0%2CC0032%3A0%2CC0025%3A0%2CC0020%3A0%2CC0037%3A0%2CC0039%3A0%2CC0036%3A0%2CC0041%3A0%2CC0042%3A0%2CC0044%3A0%2CC0043%3A0%2CC0045%3A0%2CC0046%3A0%2CC0049%3A0%2CC0047%3A0%2CC0023%3A0%2CC0056%3A0%2CC0038%3A0%2CC0082%3A0%2CC0021%3A0%2CC0026%3A0%2CC0174%3A0%2CC0177%3A0%2CC0113%3A0%2CC0089%3A0%2CC0092%3A0%2CC0190%3A0%2CC0004%3A0%2CC0022%3A0%2CC0054%3A0%2CC0179%3A0%2CC0146%3A0%2CC0052%3A0%2CC0034%3A0%2CC0063%3A0%2CC0157%3A0%2CC0003%3A0%2CC0051%3A0%2CC0136%3A0%2CC0135%3A0%2CC0007%3A0%2CSTACK1%3A0%2CSTACK42%3A0&geolocation=FR%3BGES&AwaitingReconsent=false')
    session.cookies.set('tc_ab', '0')
    session.cookies.set('__cfwaitingroom', 'ChhManVCa3BJT2RTSDZVcjRCMnhzSy93PT0SrAJoTTZRNlE0UThuQlIrVXFGdnBiWi9mQzZGUnNvOTM1Z1Z2bXBOcktlYW1ub3BmeW1maVZZNWVSd1Z3U3kyYm1jOEY4RExrNDhJRXR0bWJtQkhtcG10SXR0VDBkbTQvRGt2Tk9BanB0blhRQlhFVUpwMVNlU0EyaUMyR25RcW9IaVMwaWtpaFgrN3cvSFZRQnhDYTdrbGhPS3h2RTRtU2dvSkc3ZzlTclJodXRPMmt6d0srRnE2SE1xanNhRmUrbHJpU0dZbW82ZlJleEQxU1lTaDdZUXJSVXVlZk9KWHlGNFk0RXlFbkhXRnpsVFpjYXd5YU0yQlpqaW5nbCtHc2tQRjBtaElyaVRTdi9FdGxGMlo3K2UyN0dpYjA5UGdIMm1UbjhrdFUyV29NTT0%3D')
    session.cookies.set('tc_cj_v2_cmp', "")
    session.cookies.set('__cf_bm', 'Z3tnaUuPNNna.9hQB5ZvR91fmAdSre17xByq5xeDR.E-1686304489-0-Ab0gAeEuECiTyIqQRYkbAf4kREg8i0IAMIrhH3MiEwTgPopxyEDJiKnwkme1FEPHBi12b5MG+eMr2meCjMc/KA8=')
    session.cookies.set('FRONTONE_SESSID', 'tsc2ojnt0b93vttvmgg55anubv')
    session.cookies.set('FRONTONE_SESSION_ID', '51e30751c918db5dd4c9638b229b87289a927923')
    session.cookies.set('FRONTONE_USER', '1688843434')
    session.cookies.set('sap-closed', '1')
    session.cookies.set('tc_cj_v2_med', '')
    session.cookies.set('tc_cj_v2_ses', '') 
    session.cookies.set("TCSESSION", "1236421103410456877838")


    session.headers = headers
    response = session.get('https://www.carrefour.fr/p/liqueur-get-27-7610113019214')
    if response.status_code != 200:
        print(f"Error {response.status_code} when getting {response.url}")
        return None
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return soup

if __name__ == '__main__':
    print(get_carrefour_soup('1', proxy="http://djkofbcc:a2kk7zdq5o0e@2.56.119.93:5074"))