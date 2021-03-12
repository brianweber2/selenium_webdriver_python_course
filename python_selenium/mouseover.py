import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from config.config import CHROME_DRIVER, RAHUL_SHETTY_URL, POPUPS_URL


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/AutomationPractice/')
    action = ActionChains(CHROME_DRIVER)

    menu = CHROME_DRIVER.find_element(By.CSS_SELECTOR, '#mousehover')
    action.move_to_element(menu).perform()
    link = CHROME_DRIVER.find_element(By.LINK_TEXT, 'Reload')
    action.move_to_element(link).click().perform()

    CHROME_DRIVER.get(POPUPS_URL)
    double_click = CHROME_DRIVER.find_element(By.CSS_SELECTOR, '#double-click')
    action.double_click(double_click).perform()
    time.sleep(2)

    alert = CHROME_DRIVER.switch_to.alert
    assert 'You double clicked me!!!, You got to be kidding me' == alert.text
    alert.accept()
