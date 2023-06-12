import json
import os
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def init_driver():
    driver = webdriver.Chrome()
    return driver

def get_product_page(driver, url):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

    