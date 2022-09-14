from time import sleep

from dotenv import dotenv_values
from selenium import webdriver

from src.login import HomePage

config = dotenv_values()

driver = webdriver.Firefox()
driver.implicitly_wait(5)

home_page = HomePage(driver)
login_page = home_page.login_page()
login_page.login(config.get("USERNAME"), config.get("PASSWORD"))
sleep(50)
driver.close()
