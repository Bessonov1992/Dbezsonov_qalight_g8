from Dbezsonov_qalight_g8.HW_10.Laptop_page_rozetka import LaptopPage


class TestLaptop:
    arrow_name = ['попередньої', 'наступної']

    def test_count_items(self, chrome):
        page = LaptopPage(chrome)
        page.open()
        assert page.count_items_on_page() == 60

    def test_list_active_button(self, chrome):
        page = LaptopPage(chrome)
        page.open()
        page.scroll_to_pagination()
        assert "1" in page.active_pagination_page() and len(page.active_pagination_page()) == 1

    def test_is_arrows_status(self, chrome):
        page = LaptopPage(chrome)
        page.open()
        page.scroll_to_pagination()
        assert page.is_arrow_button_enable(self.arrow_name[0]) == False and page.is_arrow_button_enable(
            self.arrow_name[1])

    def test_count_items_on_second_page(self, chrome):
        page = LaptopPage(chrome)
        page.open()
        page.scroll_to_pagination()
        page.go_to_page(2)
        page.wait_till_page_will_be_changed(2, 5)
        assert page.count_items_on_page() == 60

    def test_list_active_button_second_page(self, chrome):
        page = LaptopPage(chrome)
        page.open()
        page.scroll_to_pagination()
        page.go_to_page(2)
        page.wait_till_page_will_be_changed(2, 5)
        page.scroll_to_pagination()
        assert "2" in page.active_pagination_page() and len(page.active_pagination_page()) == 1

    def test_current_url_was_changed(self, chrome):
        page = LaptopPage(chrome)
        page.open()
        page.scroll_to_pagination()
        page.go_to_page(2)
        page.wait_till_page_will_be_changed(2, 5)
        assert page.get_last_part_of_url() == "page=2/"
