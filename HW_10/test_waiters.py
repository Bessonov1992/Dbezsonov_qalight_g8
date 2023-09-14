from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from Dbezsonov_qalight_g8.HW_10.waiter_page_object import WaiterPage


class TestWaitersCollection:
    id_all_buttons = ["enableAfter", "colorChange", "visibleAfter"]

    def test_enable_after(self, chrome):
        page = WaiterPage(chrome)
        page.open()
        page.wait_till_be_enable(self.id_all_buttons[0], 0.5, 5)
        assert page.find_button(self.id_all_buttons[0]).is_enabled()

    def test_color_change(self, chrome):
        page = WaiterPage(chrome)
        page.open()
        tuple_with_xpath = page.make_tuple(self.id_all_buttons[1])
        is_change_color_button = WebDriverWait(chrome, 5).until(
            ec.text_to_be_present_in_element_attribute(tuple_with_xpath, "class", "mt-4 text-danger btn btn-primary"))
        assert is_change_color_button

    def test_visible_after(self, chrome):
        page = WaiterPage(chrome)
        page.open()
        page.wait_till_be_visible(self.id_all_buttons[2], 0.5, 5)
        element = page.find_button(self.id_all_buttons[2])
        assert element.is_displayed()
