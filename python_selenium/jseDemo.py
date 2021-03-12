"""
JavaScript DOM can access any elements on the web page just like how Selenium does.

Selenium has a method to execute JavaScript code in it.

Only use when Selenium is unable to execute.
"""
import time

from selenium.webdriver.common.by import By

from config.config import RAHUL_SHETTY_URL, CHROME_DRIVER


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/angularpractice')
    CHROME_DRIVER.find_element(By.NAME, 'name').send_keys('hello')
    print(CHROME_DRIVER.find_element(By.NAME, 'name').text)
    print(CHROME_DRIVER.find_element(By.NAME, 'name').get_attribute('value'))

    print(CHROME_DRIVER.execute_script('return document.getElementsByName("name")[0].value'))

    shop_button = CHROME_DRIVER.find_element(By.CSS_SELECTOR, "a[href*='shop']")
    CHROME_DRIVER.execute_script("arguments[0].click();", shop_button)

    # How to scroll in Selenium.
    CHROME_DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(5)
    CHROME_DRIVER.close()
