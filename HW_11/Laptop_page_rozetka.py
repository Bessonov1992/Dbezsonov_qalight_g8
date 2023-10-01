from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LaptopPage:
    __URL = "https://rozetka.com.ua/ua/notebooks/c80004/"

    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.__pagination_xpath = "//rz-catalog-paginator"
        self.__pagination_buttons_xpath = '//a[contains(@class,"pagination__link")]'
        self.__item_xpath = '//li[contains(@class,"catalog-grid__cell")]'
        self.__arrow_pagination_xpath = '//a[contains(@title,"{}")]'

    def open(self):
        self.__driver.get(self.__URL)

    def count_items_on_page(self) -> int:
        counter = 0
        items = self.__driver.find_elements(By.XPATH, self.__item_xpath)
        for _ in items:
            counter += 1
        return counter

    def scroll_to_pagination(self):
        button_show_more = self.__driver.find_element(By.XPATH, self.__pagination_xpath)
        _ = button_show_more.location_once_scrolled_into_view

    def is_arrow_button_enable(self, button_name: str) -> bool:
        button = self.__driver.find_element(By.XPATH, self.__arrow_pagination_xpath.format(button_name))
        if "disabled" in button.get_attribute("class"):
            return False
        else:
            return True

    def active_pagination_page(self) -> list:
        active_button_list = []
        pagination_buttons = self.__driver.find_elements(By.XPATH, self.__pagination_buttons_xpath)
        for i in pagination_buttons:
            if "active" in i.get_attribute("class"):
                active_button_list.append(i.text)
        return active_button_list

    def go_to_page(self, num_page: int):
        pagination_buttons = self.__driver.find_elements(By.XPATH, self.__pagination_buttons_xpath)
        for i in pagination_buttons:
            if str(num_page) == i.text:
                i.click()
                break

    def get_last_part_of_url(self):
        url = self.__driver.current_url.split("/")
        return url[-2] + "/"
