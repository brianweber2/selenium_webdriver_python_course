from selenium.webdriver.support.select import Select

from config.config import CHROME_DRIVER, RAHUL_SHETTY_URL


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/angularpractice/')

    dropdown = Select(CHROME_DRIVER.find_element_by_id('exampleFormControlSelect1'))
    dropdown.select_by_visible_text('Female')
    dropdown.select_by_index(0)
    # dropdown.select_by_value('M')

    CHROME_DRIVER.close()
