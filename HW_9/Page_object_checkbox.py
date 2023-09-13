from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageCheckbox:
    __URL = "https://demoqa.com/checkbox"

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def __open_close_folders(self, name, trigger):
        xpath = f'//span[text()= "{name}"]//ancestor::span/button/*[contains(@class,"icon-expand")]'
        element = self.__driver.find_element(By.XPATH, xpath)
        if trigger in element.get_attribute('class'):
            element.click()

    def open_list_of_folders(self, folders_list):
        for folder in folders_list:
            self.open_folder(folder)

    def select_list_of_targets(self, targets_list):
        for target in targets_list:
            self.select_checkbox(target)

    def __choose_dischoose_checkbox(self, name, trigger):
        xpath = f'//span[text()= "{name}"]//ancestor::span/label'
        element = self.__driver.find_element(By.XPATH, xpath)
        if trigger == "select":
            if not element.is_selected():
                while True:
                    try:
                        element.click()
                        break
                    except ElementClickInterceptedException:
                        continue
        elif trigger == "unselect":
            if element.is_selected():
                while True:
                    try:
                        element.click()
                        break
                    except ElementClickInterceptedException:
                        continue

    def find_result(self, name):
        xpath = f'//span[@class="text-success"][text()="{name}"]'
        result = self.__driver.find_element(By.XPATH, xpath).text
        return result

    def open(self):
        self.__driver.get(self.__URL)

    def open_folder(self, name):
        trigger = "close"
        self.__open_close_folders(name, trigger)

    def close_folder(self, name):
        trigger = "open"
        self.__open_close_folders(name, trigger)

    def select_checkbox(self, name):
        trigger = "select"
        self.__choose_dischoose_checkbox(name, trigger)

    def unselect_checkbox(self, name):
        trigger = "unselect"
        self.__choose_dischoose_checkbox(name, trigger)

    def list_of_selected(self, answer: list, target_list: list):
        for name in target_list:
            xpath = f'//span[text()="{name}"]'
            element = self.__driver.find_element(By.XPATH, xpath).text
            if element.capitalize() in target_list:
                answer.append(element)
