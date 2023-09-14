from Dbezsonov_qalight_g8.HW_8.page_object_radio_button import RadioButton


class TestRadioButtons:
    answer_dict_HW_8 = {}

    def test_HW_8_yes_enable(self, chrome):
        page = RadioButton(driver=chrome)
        page.open()
        page.helper_write_data(page.key_button(page.yes_radio_button), page.is_button_enabled(page.yes_radio_button),
                               page.is_button_selected(page.yes_radio_button),
                               self.answer_dict_HW_8)
        assert self.answer_dict_HW_8.get("Yes").get("is enable") == page.is_button_enabled(page.yes_radio_button)

    def test_HW_8_yes_selected(self, chrome):
        page = RadioButton(driver=chrome)
        page.open()
        page.set_button(page.yes_radio_button)
        page.helper_write_data(page.key_button(page.yes_radio_button), page.is_button_enabled(page.yes_radio_button),
                               page.is_button_selected(page.yes_radio_button),
                               self.answer_dict_HW_8)
        assert self.answer_dict_HW_8.get("Yes").get("is selected") == page.is_button_selected(page.yes_radio_button)

    def test_HW_8_impressive_enable(self, chrome):
        page = RadioButton(driver=chrome)
        page.open()
        page.helper_write_data(page.key_button(page.impressive_radio_button),
                               page.is_button_enabled(page.impressive_radio_button),
                               page.is_button_selected(page.impressive_radio_button),
                               self.answer_dict_HW_8)
        assert self.answer_dict_HW_8.get("Impressive").get("is enable") == page.is_button_enabled(
            page.impressive_radio_button)

    def test_HW_8_impressive_selected(self, chrome):
        page = RadioButton(driver=chrome)
        page.open()
        page.helper_write_data(page.key_button(page.impressive_radio_button),
                               page.is_button_enabled(page.impressive_radio_button),
                               page.is_button_selected(page.impressive_radio_button),
                               self.answer_dict_HW_8)
        assert self.answer_dict_HW_8.get("Impressive").get("is selected") == page.is_button_selected(
            page.impressive_radio_button)

    def test_HW_8_no_enable(self, chrome):
        page = RadioButton(driver=chrome)
        page.open()
        page.helper_write_data(page.key_button(page.no_radio_button), page.is_button_enabled(page.no_radio_button),
                               page.is_button_selected(page.no_radio_button),
                               self.answer_dict_HW_8)
        assert self.answer_dict_HW_8.get("No").get("is enable") == page.is_button_enabled(page.no_radio_button)

    def test_HW_8_no_selected(self, chrome):
        page = RadioButton(driver=chrome)
        page.open()
        page.helper_write_data(page.key_button(page.no_radio_button), page.is_button_enabled(page.no_radio_button),
                               page.is_button_selected(page.no_radio_button),
                               self.answer_dict_HW_8)
        assert self.answer_dict_HW_8.get("No").get("is selected") == page.is_button_selected(page.no_radio_button)