from selenium import webdriver
from selenium.webdriver.common.by import By


class Loginpage:
    username_by_xpath="//input[@placeholder='Email']"
    password_by_xpath="//input[@name='password']"
    submit_by_xpath="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver


    def setusername(self,username):
        self.driver.find_element(By.XPATH,self.username_by_xpath).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.password_by_xpath).send_keys(password)

    def clickloginbutton(self):
        self.driver.find_element(By.XPATH,self.submit_by_xpath).click()