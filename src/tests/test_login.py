from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from src.login import HomePage


def test_login_page(driver):
    home_page = HomePage(driver)
    login_page = home_page.login_page()
    login_page.login("esquinadosertaojp@gmail.com", "gmES1947&")

    errors = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.XPATH, '//button[normalize-space()="Only allow essential cookies"]')
        ))

    assert len(errors) == 0
