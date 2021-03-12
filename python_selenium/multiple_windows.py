from selenium.webdriver.common.by import By

from config.config import CHROME_DRIVER, HEROKUAPP_URL


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{HEROKUAPP_URL}/windows')
    CHROME_DRIVER.find_element(By.LINK_TEXT, 'Click Here').click()

    windows = CHROME_DRIVER.window_handles
    parent_window = windows[0]
    child_window = windows[1]

    CHROME_DRIVER.switch_to.window(child_window)
    child_h3_text = CHROME_DRIVER.find_element(By.TAG_NAME, 'h3').text
    print(child_h3_text)
    CHROME_DRIVER.close()  # close child window.
    CHROME_DRIVER.switch_to.window(parent_window)
    parent_h3_text = CHROME_DRIVER.find_element(By.TAG_NAME, 'h3').text
    print(parent_h3_text)
    CHROME_DRIVER.close()  # close parent window.

    assert 'Opening a new window' == parent_h3_text
    assert 'New Window' == child_h3_text
