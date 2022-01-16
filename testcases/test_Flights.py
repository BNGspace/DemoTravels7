import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from PageObjects.Flightspage import FlightsSelect
from PageObjects.LoginPage import Loginpage
from utilites.CustomLogging import Logs
from utilites.readProperties import ReadConfig

class Test_003_login:

    baseURL =ReadConfig.getURL()
    username =ReadConfig.getemail()
    password =ReadConfig.getpassword()
    logger = Logs.loggen()

    @pytest.mark.regression
    def test_Flightpageload(self,setup):
        self.logger.info("***********Verifying Login Functionality *******")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.LP = Loginpage(self.driver)
        self.LP.setusername(self.username)
        self.LP.setpassword(self.password)
        self.LP.clickloginbutton()

        self.FL=FlightsSelect(self.driver)
        self.FL.ClickonFlights()


        bestflight=self.driver.find_element(By.CSS_SELECTOR,"h2[class='text-center']").text
        print(bestflight)
        if bestflight == "RENTAL BEST CARS TODAY":
            assert True
            self.logger.info("**************Home Flightpageload is Passed ******")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Flightpageload.png")
            self.driver.close()
            self.logger.error("**************Flightpageload is Failed *****")
            assert False
