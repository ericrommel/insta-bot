import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import dotenv_values

LOGGER = logging.getLogger(__name__)

config = dotenv_values(".env")


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def allow_cookies(self):
        LOGGER.info('Handle "Allow Cookies" popup if it appears')
        allow_cookies_popup = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//button[normalize-space()="Only allow essential cookies"]')
            ))
        if allow_cookies_popup:
            LOGGER.info('Click on "Only allow essential cookies button"')
            allow_cookies_popup.click()

    def login(self, username, password):
        self.allow_cookies()
        LOGGER.info('Log in to Instagram page')
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[name='username']")
            )
        )
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[name='password']")
            )
        )

        LOGGER.info('Typing username and password')
        username_input.send_keys(username)
        password_input.send_keys(password)

        LOGGER.info('Pressing Log In button')
        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                # (By.XPATH, "//button[@type='submit']")
                (By.XPATH, '//button[normalize-space()="Only allow essential cookies"]')
            )
        )
        login_button.click()


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        print(config.get("INSTAGRAM"))
        driver.get(config.get("INSTAGRAM"))

    def login_page(self):
        return LoginPage(self.driver)
