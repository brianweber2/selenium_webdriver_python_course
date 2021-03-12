"""
https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from config.config import RAHUL_SHETTY_URL,  CHROME_DRIVER_EXECUTABLE_PATH


if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--headless')

    service = Service(executable_path=CHROME_DRIVER_EXECUTABLE_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(f'{RAHUL_SHETTY_URL}/angularpractice')
    print(driver.title)

    time.sleep(5)
    driver.close()
