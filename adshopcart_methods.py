import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import adshopcart_locators as locators
from html import unescape

s = Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print("\n")
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.aos_url)

    if driver.current_url == locators.aos_url and driver.title == unescape(locators.aos_home_page_title):
        print(f'Hello! {locators.app} website launched successfully!\n')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        print("\n")
        sleep(2)
    else:
        print(f'{locators.app} did not launch. Check your code or application.')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print("\n")
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(5)
        driver.close()
        driver.quit()

setUp()
tearDown()