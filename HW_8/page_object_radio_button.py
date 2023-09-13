from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:
    __URL = "https://demoqa.com/radio-button"

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.yes_radio_button = 'yesRadio'
        self.impressive_radio_button = 'impressiveRadio'
        self.no_radio_button = 'noRadio'

    def open(self):
        self.__driver.get(self.__URL)

    @staticmethod
    def helper_write_data(main_key: str, enable: bool, selected: bool, dictionary: dict):
        tmp_dict = {"is enable": enable, "is selected": selected}
        dictionary[main_key] = tmp_dict

    def __select_button_by_locator(self, xpath):
        self.__driver.find_element(By.XPATH, xpath).click()

    def __check_button_selected(self, xpath):
        return self.__driver.find_element(By.XPATH, xpath).is_selected()

    def __check_button_enabled(self, xpath):
        return self.__driver.find_element(By.XPATH, xpath).is_enabled()

    def __get_name(self, xpath):
        return self.__driver.find_element(By.XPATH, xpath).text

    def select_button(self, name):
        locator = f"//label[@for='{name}']//ancestor::div[contains(@class,'radio')]/label"
        self.__select_button_by_locator(locator)

    def is_button_selected(self, name) -> bool:
        locator = f"//label[@for='{name}']//ancestor::div[contains(@class,'radio')]/input"
        return self.__check_button_selected(locator)

    def is_button_enabled(self, name) -> bool:
        locator = f"//label[@for='{name}']//ancestor::div[contains(@class,'radio')]/input"
        return self.__check_button_enabled(locator)

    def key_button(self, name):
        locator = f"//label[@for='{name}']//ancestor::div[contains(@class,'radio')]/label"
        return self.__get_name(locator)

    def set_button(self, name):
        locator = f"//label[@for='{name}']//ancestor::div[contains(@class,'radio')]/label"
        self.__driver.find_element(By.XPATH, locator).click()
