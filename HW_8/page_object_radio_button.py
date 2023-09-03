from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:
    __URL = "https://demoqa.com/radio-button"

    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def open(self):
        self.__driver.get(self.__URL)
        self.__yes_radio_button_xpass = "//label[@for='yesRadio']//ancestor::div[contains(@class,'radio')]"
        self.__impressive_radio_button_xpass = "//label[@for='impressiveRadio']//ancestor::div[contains(@class," \
                                               "'radio')] "
        self.__no_radio_button_xpass = "//label[@for='noRadio']//ancestor::div[contains(@class,'radio')]"

    def helper_write_data(self, main_key: str, enable: bool, selected: bool, dictionary: dict):
        tmp_dict = {"is enable": enable, "is selected": selected}
        dictionary[main_key] = tmp_dict

    def __select_button_by_locator(self, xpass):
        self.__driver.find_element(By.XPATH, xpass).click()

    def __check_button_selected(self, xpass):
        return self.__driver.find_element(By.XPATH, xpass).is_selected()

    def __check_button_enabled(self, xpass):
        return self.__driver.find_element(By.XPATH, xpass).is_enabled()

    def __get_name(self, xpass):
        return self.__driver.find_element(By.XPATH, xpass).text

    def select_yes_button(self):
        locator = self.__yes_radio_button_xpass + "/label"
        self.__select_button_by_locator(locator)

    def select_impressive_button(self):
        locator = self.__impressive_radio_button_xpass + "/label"
        self.__select_button_by_locator(locator)

    def select_no_button(self):
        locator = self.__no_radio_button_xpass + "/label"
        self.__select_button_by_locator(locator)

    def is_yes_button_selected(self) -> bool:
        locator = self.__yes_radio_button_xpass + "/input"
        return self.__check_button_selected(locator)

    def is_impressive_button_selected(self) -> bool:
        locator = self.__impressive_radio_button_xpass + "/input"
        return self.__check_button_selected(locator)

    def is_no_button_selected(self) -> bool:
        locator = self.__no_radio_button_xpass + "/input"
        return self.__check_button_selected(locator)

    def is_yes_button_enabled(self) -> bool:
        locator = self.__yes_radio_button_xpass + "/input"
        return self.__check_button_enabled(locator)

    def is_impressive_button_enabled(self) -> bool:
        locator = self.__impressive_radio_button_xpass + "/input"
        return self.__check_button_enabled(locator)

    def is_no_button_enabled(self) -> bool:
        locator = self.__no_radio_button_xpass + "/input"
        return self.__check_button_enabled(locator)

    def key_yes(self):
        locator = self.__yes_radio_button_xpass + "/label"
        return self.__get_name(locator)

    def key_impressive(self):
        locator = self.__impressive_radio_button_xpass + "/label"
        return self.__get_name(locator)

    def key_no(self):
        locator = self.__no_radio_button_xpass + "/label"
        return self.__get_name(locator)

    def set_yes(self):
        locator = self.__yes_radio_button_xpass + "/label"
        self.__driver.find_element(By.XPATH, locator).click()

    def set_impressive(self):
        locator = self.__impressive_radio_button_xpass + "/label"
        self.__driver.find_element(By.XPATH, locator).click()

    def set_no(self):
        locator = self.__no_radio_button_xpass + "/label"
        self.__driver.find_element(By.XPATH, locator).click()