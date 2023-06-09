from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def init_driver():
    driver = webdriver.Chrome()
    return driver

def get_product_page(driver, url):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'onetrust-reject-all-handler').click()

    # asking server for a new journey id
    journey_id = driver.execute_script(
        """
            journey_id = await fetch("https://www.auchan.fr/journey/update", {
                "headers": {
                    "accept": "application/json",
                    "accept-language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                    "content-type": "application/x-www-form-urlencoded",
                    "sec-ch-ua": "Not.A/Brand;v=8, Chromium;v=114, Google Chrome;v=114",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "x-requested-with": "XMLHttpRequest"
                },
                "referrer": "https://www.auchan.fr/get-27-liqueur-a-base-de-menthe-17-9/pr-C1586720",
                "referrerPolicy": "strict-origin-when-cross-origin",
                "body": "offeringContext.seller.id=ddfaf8fc-b37b-4e83-9bc1-d32f3566dccc&offeringContext.channels%5B0%5D=PICK_UP&offeringContext.storeReference=889&address.zipcode=54000&address.city=Nancy&address.country=France&location.latitude=48.69372222373215&location.longitude=6.183409641594068&accuracy=MUNICIPALITY&position=1&journeyId=defa0178-defa-defa-defa-defa01720217",
                "method": "POST",
                "mode": "cors",
                "credentials": "include"
                }).then((response) => response.json())
                .then((data) => (data['id']));
            return journey_id;
        """
    )
    return journey_id
    

if __name__ == '__main__':
    driver = init_driver()
    get_product_page(driver, 'https://www.auchan.fr/get-27-liqueur-a-base-de-menthe-17-9/pr-C1586720')
    
    while True:
        pass

