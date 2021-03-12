from selenium.webdriver.common.by import By

from config.config import CHROME_DRIVER, HEROKUAPP_URL


if __name__ == '__main__':
    # frame, iframe, frameset
    CHROME_DRIVER.get(f'{HEROKUAPP_URL}/iframe')
    CHROME_DRIVER.switch_to.frame('mce_0_ifr')
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, '#tinymce').clear()
    CHROME_DRIVER.find_element(By.CSS_SELECTOR, '#tinymce').send_keys('I am able to automate!')

    CHROME_DRIVER.switch_to.default_content()
    print(CHROME_DRIVER.find_element(By.TAG_NAME, 'h3').text)

    CHROME_DRIVER.close()
