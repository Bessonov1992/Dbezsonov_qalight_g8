from Dbezsonov_qalight_g8.HW_9.Page_object_checkbox import PageCheckbox


class TestCheckbox:

    def test_1(self, chrome):
        final_result = []
        folders = ["Home", "Documents", "Office"]
        targets = ["Public", "Private"]
        page = PageCheckbox(chrome)
        page.open()
        page.open_list_of_folders(folders)
        page.select_list_of_targets(targets)
        page.list_of_selected(final_result, targets)
        assert targets == final_result
