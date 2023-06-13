# price_scraping

This project is a tool that allows you to retrieve the prices of a product from all of the stores of most of the major French retail chains.

## Installation

Clone the repo and run 
    
    pip install -r requirements.txt

Examples of usage are available at the end of each file.

## How it works
### **Auchan**

The store of reference is tracked by their servers. We first ask for a journey_id from their servers and then we can update the store from which we want to retrieve the prices with a request containing the journey_id and the store information.

The information about the stores nearby a location can be retrieved by sending a request to their API with its latitude and longitude. To get all the stores on the territory, we send a request with the latitude and longitude of the 500-ish biggest French cities and add their information to a set.

The requests are sent to the API with the `requests` library and the prices are read from the page using `Selenium` because Javascript had to be enabled to load them.

### **Colruyt**

The ids of all the stores are retrieved from their API with a single request.

The store of reference is updated by sending a request to their API with the store_id.

The price is parsed from the html response of a request to the product page and decoded from base64.

We are getting IP blocked after a few requests, so we are using rotating proxies from `proxies.json` to bypass this.

### **Carrefour**

The store_ids are retrieved from their API with a bunch of requests. 

The store of reference is saved using a cookie. 

We get the product page with `Selenium` and then iterate over the store_ids, updating the cookie to switch stores and then reading the price from the page.

### **Cora**

The store ids are roughly contained between 70 and 170.

The store of reference is saved using a cookie.

We get the product page with `Selenium` and then iterate over the store_ids, updating the cookie to switch stores and then reading the price from the page.

### **Intermarché**

The ids of all the stores are retrieved from their API with a single request.

The price is parsed from the JSON response of a request containing the store_id to their API. (This request might be blocked by a Captcha, if so, using `Selenium` with an existing Chrome profile should work thanks to reCaptcha.)

### **Match**

The store ids are retrieved from their API with a single request.

The prices are retrieved from their API with a request containing the product_id and the store_id.

### **Super U**

(Blocked by captcha, might be possible to bypass with `Selenium` and an existing Chrome profile but I was lazy.)

The store ids can be parsed from the JSON response to a request on their API.

The store of reference is saved on their servers and can be updated by sending a request to their API with the store_id.

The price is parsed from the product page.

