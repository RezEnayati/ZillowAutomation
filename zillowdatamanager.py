import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"

class DataManager():
    def __init__(self):
        response = requests.get(URL)
        zillow_webpage = response.text
        self.soup = BeautifulSoup(zillow_webpage, "html.parser")
        self.url_list = []
        self.price_list = []
        self.address_list = []
        self.get_url_list()
        self.get_price_list()
        self.get_address_list()

    def get_url_list(self):
        url_l = self.soup.select(".StyledPropertyCardDataArea-anchor")
        self.url_list = [url.get("href") for url in url_l]

    def get_price_list(self):
        price_l = self.soup.select(".PropertyCardWrapper__StyledPriceLine")
        self.price_list = [price.getText().split("/")[0].split("+")[0] for price in price_l]

    def get_address_list(self):
        address_l = self.soup.select(".StyledPropertyCardDataArea-anchor")
        self.address_list = [address.getText().strip() for address in address_l]
