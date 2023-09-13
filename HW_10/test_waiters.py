from Dbezsonov_qalight_g8.HW_10.waiter_page_object import WaiterPage


class TestWaitersCollection:

    def test_1(self, chrome):
        page = WaiterPage(chrome)
        page.open()
