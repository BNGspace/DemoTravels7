from selenium import webdriver
from selenium.webdriver.common.by import By


class Carpage:

    hotels_by_xpath="//a[text()='Hotels']"

    def __init__(self,driver):
        self.driver=driver

    def clickoncars(self):
        self.driver.find_element(By.XPATH,self.hotels_by_xpath).click()
