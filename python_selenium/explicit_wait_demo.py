import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import CHROME_DRIVER, RAHUL_SHETTY_URL


if __name__ == '__main__':
    product_names_in_cart = []

    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/seleniumPractise/')
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, 'input.search-keyword').send_keys('ber')

    time.sleep(4)

    products = CHROME_DRIVER.find_elements(By.XPATH, "//div[@class='products']/div")
    assert len(products) == 3

    # Add products to cart.
    buttons = CHROME_DRIVER.find_elements(By.XPATH, "//div[@class='product-action']/button")
    for button in buttons:
        product_names_in_cart.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
        button.click()
    print(product_names_in_cart)

    # Proceed to checkout.
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
    CHROME_DRIVER.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
    wait = WebDriverWait(CHROME_DRIVER, 10)  # Explicit waiting with specific conditions for specific elements.
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "promoCode"))
    )
    veggies = CHROME_DRIVER.find_elements(By.CSS_SELECTOR, 'p.product-name')
    product_names_on_cart_page = [v.text for v in veggies]
    print(product_names_on_cart_page)
    assert product_names_in_cart == product_names_on_cart_page

    # Apply discount.
    original_amount = float(CHROME_DRIVER.find_element(By.CSS_SELECTOR, '.discountAmt').text)
    print(f'Original amount: ${original_amount}')
    CHROME_DRIVER.find_element(By.CLASS_NAME, 'promoCode').send_keys('rahulshettyacademy')
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, '.promoBtn').click()
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo"))
    )
    discount_amount = float(CHROME_DRIVER.find_element(By.CSS_SELECTOR, '.discountAmt').text)
    print(f'Discount amount: ${discount_amount}')
    assert discount_amount < original_amount
    discount_success_text = CHROME_DRIVER.find_element(By.CSS_SELECTOR, 'span.promoInfo').text
    print(discount_success_text)

    amounts = [float(amount.text) for amount in CHROME_DRIVER.find_elements(By.XPATH, '//tr/td[5]/p')]
    amounts_sum = sum(amounts)
    print(amounts_sum)
    total_amount = float(CHROME_DRIVER.find_element(By.CSS_SELECTOR, '.totAmt').text)
    print(total_amount)
    assert amounts_sum == total_amount

    CHROME_DRIVER.close()
