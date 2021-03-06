import time

from config.config import CHROME_DRIVER, RAHUL_SHETTY_URL


if __name__ == '__main__':
    CHROME_DRIVER.implicitly_wait(5)  # Implicit wait - wait until 5 seconds if object is not displayed (Global wait)
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
    # Apply discount.
    CHROME_DRIVER.find_element_by_class_name('promoCode').send_keys('rahulshettyacademy')
    CHROME_DRIVER.find_element_by_css_selector('.promoBtn').click()
    discount_success_text = CHROME_DRIVER.find_element_by_css_selector('span.promoInfo').text

    CHROME_DRIVER.close()
