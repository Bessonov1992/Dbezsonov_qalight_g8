import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def chrome():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/text-box")
    yield driver
    driver.quit()