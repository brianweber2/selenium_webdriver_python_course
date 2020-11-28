from config.config import CHROME_DRIVER, RAHUL_SHETTY_URL


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/AutomationPractice/')
    checkboxes = CHROME_DRIVER.find_elements_by_xpath("//input[@type='checkbox']")
    print(len(checkboxes))
    for checkbox in checkboxes:
        if checkbox.get_attribute('value') == 'option2':
            checkbox.click()
            assert checkbox.is_selected()
    CHROME_DRIVER.close()
