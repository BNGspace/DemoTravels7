import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from PageObjects.Hotels import Hotelpage
from PageObjects.LoginPage import Loginpage
from utilites.CustomLogging import Logs
from utilites.readProperties import ReadConfig

class Test_002_login:

    baseURL =ReadConfig.getURL()
    username =ReadConfig.getemail()
    password =ReadConfig.getpassword()
    logger = Logs.loggen()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_hotelpageload(self,setup):
        self.logger.info("***********Verifying Login Functionality *******")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.LP = Loginpage(self.driver)
        self.LP.setusername(self.username)
        self.LP.setpassword(self.password)
        self.LP.clickloginbutton()

        self.HP = Hotelpage(self.driver)
        self.HP.click0nhotels()

        besthotels = self.driver.find_element(By.CSS_SELECTOR, "h2[class='text-center']").text
        if besthotels == "SEARCH FOR BEST HOTELS":
            assert True
            self.logger.info("**************Hotelpageloadd is Passed ******")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Hotelpageload.png")
            self.driver.close()
            self.logger.error("**************Hotelpageload is Failed *****")
            assert False

