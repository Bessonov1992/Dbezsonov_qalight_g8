from selenium.webdriver.remote.webdriver import WebDriver


class WaiterPage:
    __URL = "https://demoqa.com/dynamic-properties"

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def open(self):
        self.__driver.get(self.__URL)
