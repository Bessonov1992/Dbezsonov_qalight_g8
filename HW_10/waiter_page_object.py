import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class WaiterPage:
    __URL = "https://demoqa.com/dynamic-properties"

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.button_xpath = '//button[@type][@id="{}"]'

    def open(self):
        self.__driver.get(self.__URL)

    def find_button(self, element_id: str) -> WebElement:
        element = self.__driver.find_element(By.XPATH, self.button_xpath.format(element_id))
        return element

    def make_tuple(self, element_id: str) -> tuple:
        tuple_with_xpath = (By.XPATH, self.button_xpath.format(element_id))
        return tuple_with_xpath

    def wait_till_be_enable(self, element_id: str, wait: float, max_wait_time: float):
        element = self.__driver.find_element(By.XPATH, self.button_xpath.format(element_id))
        end_time = time.monotonic() + max_wait_time
        while time.monotonic() < end_time:
            if element.is_enabled():
                break
            else:
                time.sleep(wait)
                continue

    def wait_till_be_visible(self, element_id: str, wait: float, max_wait_time: float):
        end_time = time.monotonic() + max_wait_time
        while time.monotonic() < end_time:
            try:
                self.__driver.find_element(By.XPATH, self.button_xpath.format(element_id))
                break
            except NoSuchElementException:
                time.sleep(wait)
                continue
