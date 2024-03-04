from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://docs.google.com/forms/d/e/1FAIpQLSckhluRLOb2DgY4SZU8tpj-4Smc7ieOAz5AJvUrG55bzfdJ_g/viewform?usp=sf_link"


class FormFiller():
    def __init__(self, listing_data:list):
        self.listing_data = listing_data
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url=URL)
        self.fill_form()

    def fill_form(self):

        for data in self.listing_data:
            address_input = self.driver.find_element(By.XPATH,
                                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = self.driver.find_element(By.XPATH,
                                                   value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            url_input = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH,
                                                     value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            time.sleep(10)
            address_input.send_keys(data.address)
            time.sleep(1)
            print(data.price)
            price_input.send_keys(data.price)
            time.sleep(1)
            url_input.send_keys(data.url)
            time.sleep(1)
            submit_button.click()
            time.sleep(5)
            another_button = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_button.click()
        print("Form has been completed")

