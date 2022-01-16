import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="C:\\workse\\chromedriver.exe")
        driver.maximize_window()
        print("Launching Chrome Browser************")
    elif browser == 'edge':
            driver = webdriver.Edge(executable_path="C:\\workse\\msedgedriver.exe")
            driver.maximize_window()
            print("Launching Edge Browser************")
    else:
        driver = webdriver.Chrome(executable_path="C:\\workse\\chromedriver.exe")
        driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")