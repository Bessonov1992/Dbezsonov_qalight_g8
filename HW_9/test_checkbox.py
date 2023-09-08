from Dbezsonov_qalight_g8.HW_9.Page_object_checkbox import PageCheckbox


class TestCheckbox:

    def test_1(self, chrome):
        folders = ["Home", "Documents", "Office"]
        targets = ["Public", "Private"]
        page = PageCheckbox(chrome)
        page.open()
        for folder in folders:
            page.open_folder(folder)
        for target in targets:
            page.select_checkbox(target)
            print(page.check_result(target.lower()))
            print(target.lower())
            assert page.check_result(target.lower()) == target.lower()


