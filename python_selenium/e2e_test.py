from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config.config import RAHUL_SHETTY_URL, CHROME_DRIVER


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/angularpractice/')
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

    products = CHROME_DRIVER.find_elements(By.XPATH, "//div[@class='card h-100']")
    for product in products:
        product_name = product.find_element(By.XPATH, "div/h4/a").text
        if product_name == 'Blackberry':
            product.find_element(By.XPATH, 'div/button').click()

    # Cart button
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    # Checkout button
    CHROME_DRIVER.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    CHROME_DRIVER.find_element(By.ID, 'country').send_keys('ind')
    wait = WebDriverWait(CHROME_DRIVER, 7)
    wait.until(
        expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India'))
    )
    CHROME_DRIVER.find_element(By.LINK_TEXT, 'India').click()
    terms_checkbox = CHROME_DRIVER.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    terms_checkbox.click()

    # Purchase button
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    alert = CHROME_DRIVER.find_element(By.CLASS_NAME, 'alert-success')

    assert 'Success! Thank you!' in alert.text

    CHROME_DRIVER.get_screenshot_as_file('screen.png')

    CHROME_DRIVER.close()
