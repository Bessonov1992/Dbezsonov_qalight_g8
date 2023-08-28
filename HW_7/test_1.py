from selenium.webdriver.common.by import By
import logging


def test_1(chrome):
    test_name, test_email, test_curr_adr, test_perm_adr = "Dmytro", "Dmytro@gmail.com", "Kyiv", "Kyiv, Kyrylivska street"
    chrome.find_element(By.XPATH, '//input[@id="userName"]').send_keys(test_name)
    chrome.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys(test_email)
    chrome.find_element(By.XPATH, '//textarea[@id="currentAddress"]').send_keys(test_curr_adr)
    chrome.find_element(By.XPATH, '//textarea[@id="permanentAddress"]').send_keys(test_perm_adr)
    chrome.find_element(By.XPATH, '//button[@id="submit"]').click()
    # тести для перевірки введенних данних
    name = chrome.find_element(By.XPATH, '//p[@id="name"]').text
    email = chrome.find_element(By.XPATH, '//p[@id="email"]').text
    curr_adr = chrome.find_element(By.XPATH, '//p[@id="currentAddress"]').text
    perm_adr = chrome.find_element(By.XPATH, '//p[@id="permanentAddress"]').text

    assert name == "Name:" + test_name, "wrong name"
    assert email == "Email:" + test_email, "wrong email"
    assert curr_adr == "Current Address :" + test_curr_adr, "wrong Current Address"
    assert perm_adr == "Permananet Address :" + test_perm_adr, "wrong Permananet Address"
    logging.info(name)
    logging.info(email)
    logging.info(curr_adr)
    logging.info(perm_adr)
