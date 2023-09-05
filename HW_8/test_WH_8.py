from Dbezsonov_qalight_g8.HW_8.page_object_radio_button import RadioButton


class TestRadioButtons:
    answer_dict_HW_8 = {}


    def test_HW_8_yes_enable(self, chrome):
        page = RadioButton(driver=chrome)
        page.open()
        page.set_yes()
        page.helper_write_data(page.key_yes(), page.is_yes_button_enabled(), page.is_yes_button_selected(),
                               self.answer_dict_HW_8)
        assert self.answer_dict_HW_8.get("Yes").get("is enable") == page.is_yes_button_enabled()

    def test_HW_8_yes_selected(self, chrome):
        page = RadioButton(driver=chrome)
        assert self.answer_dict_HW_8.get("Yes").get("is selected") == page.is_yes_button_selected()

    def test_HW_8_impressive_enable(self, chrome):
        page = RadioButton(driver=chrome)
        page.helper_write_data(page.key_impressive(), page.is_impressive_button_enabled(),
                               page.is_impressive_button_selected(),
                               self.answer_dict_HW_8)
        assert self.answer_dict_HW_8.get("Impressive").get("is enable") == page.is_impressive_button_enabled()

    def test_HW_8_impressive_selected(self, chrome):
        page = RadioButton(driver=chrome)
        assert self.answer_dict_HW_8.get("Impressive").get("is selected") == page.is_impressive_button_selected()

    def test_HW_8_no_enable(self, chrome):
        page = RadioButton(driver=chrome)
        page.helper_write_data(page.key_no(), page.is_no_button_enabled(), page.is_no_button_selected(),
                               self.answer_dict_HW_8)
        assert self.answer_dict_HW_8.get("No").get("is enable") == page.is_no_button_enabled()

    def test_HW_8_no_selected(self, chrome):
        page = RadioButton(driver=chrome)
        assert self.answer_dict_HW_8.get("No").get("is selected") == page.is_no_button_selected()
