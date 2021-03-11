import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import CHROME_DRIVER, RAHUL_SHETTY_URL


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/seleniumPractise/')
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, 'input.search-keyword').send_keys('ber')

    time.sleep(4)

    products = CHROME_DRIVER.find_elements(By.XPATH, "//div[@class='products']/div")
    assert len(products) == 3

    # Add products to cart.
    buttons = CHROME_DRIVER.find_elements(By.XPATH, "//div[@class='product-action']/button")
    for button in buttons:
        button.click()

    # Proceed to checkout.
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
    CHROME_DRIVER.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
    wait = WebDriverWait(CHROME_DRIVER, 10)  # Explicit waiting with specific conditions for specific elements.
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "promoCode"))
    )
    # Apply discount.
    CHROME_DRIVER.find_element(By.CLASS_NAME, 'promoCode').send_keys('rahulshettyacademy')
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, '.promoBtn').click()

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo"))
    )
    discount_success_text = CHROME_DRIVER.find_element(By.CSS_SELECTOR, 'span.promoInfo').text

    CHROME_DRIVER.close()
