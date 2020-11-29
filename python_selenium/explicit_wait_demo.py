import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import CHROME_DRIVER, RAHUL_SHETTY_URL


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/seleniumPractise/')
    CHROME_DRIVER.find_element_by_css_selector('input.search-keyword').send_keys('ber')

    time.sleep(4)

    products = CHROME_DRIVER.find_elements_by_xpath("//div[@class='products']/div")
    assert len(products) == 3

    # Add products to cart.
    buttons = CHROME_DRIVER.find_elements_by_xpath("//div[@class='product-action']/button")
    for button in buttons:
        button.click()

    # Proceed to checkout.
    CHROME_DRIVER.find_element_by_css_selector("img[alt='Cart']").click()
    CHROME_DRIVER.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
    wait = WebDriverWait(CHROME_DRIVER, 10)  # Explicit waiting with specific conditions for specific elements.
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "promoCode"))
    )
    # Apply discount.
    CHROME_DRIVER.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
    CHROME_DRIVER.find_element_by_css_selector('.promoBtn').click()

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo"))
    )
    discount_success_text = CHROME_DRIVER.find_element_by_css_selector('span.promoInfo').text

    CHROME_DRIVER.close()
