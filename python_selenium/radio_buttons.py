from config.config import CHROME_DRIVER, RAHUL_SHETTY_URL


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/AutomationPractice/')
    radio_buttons = CHROME_DRIVER.find_elements_by_name('radioButton')
    print(len(radio_buttons))
    radio_buttons[2].click()
    assert radio_buttons[2].is_selected()
    CHROME_DRIVER.close()
