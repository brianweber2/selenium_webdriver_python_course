from config.config import CHROME_DRIVER, RAHUL_SHETTY_URL


validate_text = 'Option3'


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/AutomationPractice/')
    CHROME_DRIVER.find_element_by_css_selector('#name').send_keys('Option3')
    CHROME_DRIVER.find_element_by_id('alertbtn').click()
    alert = CHROME_DRIVER.switch_to.alert
    alert_text = alert.text
    assert validate_text in alert_text
    alert.accept()  # Left button
    # alert.dismiss()  # Right button
    CHROME_DRIVER.close()
