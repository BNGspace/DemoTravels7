import time
from selenium import webdriver
import pytest
from PageObjects.LoginPage import Loginpage
from utilites.CustomLogging import Logs
from utilites.readProperties import ReadConfig

class Test_001_login:

    baseURL =ReadConfig.getURL()
    username =ReadConfig.getemail()
    password =ReadConfig.getpassword()
    logger = Logs.loggen()

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_homepageTitle(self,setup):
        self.logger.info("************** Test_001_Login ***********")
        self.logger.info("**************Verifying Home Page Title*******")

        self.driver = setup
        self.driver.get(self.baseURL)
        pagetitle=self.driver.title
        if pagetitle=="Login - PHPTRAVELS":
            self.driver.close()
            self.logger.info("**************Home Page Title is Passed *******")
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "Test_homepageTitle.png")
            self.driver.close()
            self.logger.error("**************Home Page Title is Failed ********")
            assert False

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_loginfunction(self,setup):
        self.logger.info("***********Verifying Login Functionality *******")
        self.driver=setup

        self.driver.get(self.baseURL)
        self.LP=Loginpage(self.driver)
        self.LP.setusername(self.username)
        self.LP.setpassword(self.password)
        self.LP.clickloginbutton()

        hometitle = self.driver.title
        if hometitle=="Dashboard - PHPTRAVELS":
            assert True
            self.logger.info("**************Home Login Test is Passed ******")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Loginfunction.png")
            self.driver.close()
            self.logger.error("**************Home Login Test is Failed *****")
            assert False

