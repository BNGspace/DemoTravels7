import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from PageObjects.Cars import Carpage
from PageObjects.LoginPage import Loginpage
from utilites.CustomLogging import Logs
from utilites.readProperties import ReadConfig

class Test_004_login:

    baseURL =ReadConfig.getURL()
    username =ReadConfig.getemail()
    password =ReadConfig.getpassword()
    logger = Logs.loggen()

    @pytest.mark.regression
    def test_Carspageload(self,setup):
        self.logger.info("***********Verifying Login Functionality *******")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.LP = Loginpage(self.driver)
        self.LP.setusername(self.username)
        self.LP.setpassword(self.password)
        self.LP.clickloginbutton()

        self.CP=Carpage(self.driver)
        self.CP.clickoncars()


        bestcars=self.driver.title
        print(bestcars)
        if bestcars == "Search Hotels - PHPTRAVELS":
            assert True
            self.logger.info("**************Home Carspageload is Passed ******")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Carspageload.png")
            self.driver.close()
            self.logger.error("**************Carspageload is Failed *****")
            assert False
