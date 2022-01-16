from selenium import webdriver
from selenium.webdriver.common.by import By


class FlightsSelect:

    Flights_by_xpath="//a[@href='https://www.phptravels.net/cars']"

    def __init__(self,driver):
        self.driver=driver

    def ClickonFlights(self):
        self.driver.find_element(By.XPATH,self.Flights_by_xpath).click()
