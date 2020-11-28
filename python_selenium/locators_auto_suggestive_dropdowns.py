import time

from config.config import CHROME_DRIVER, RAHUL_SHETTY_URL


if __name__ == '__main__':
    CHROME_DRIVER.get(f'{RAHUL_SHETTY_URL}/dropdownsPractise/')
    CHROME_DRIVER.find_element_by_id('autosuggest').send_keys('ind')
    time.sleep(2)
    countries = CHROME_DRIVER.find_elements_by_css_selector("li[class='ui-menu-item'] a")
    print(len(countries))
    for country in countries:
        if country.text == 'India':
            country.click()
            break
    assert CHROME_DRIVER.find_element_by_id("autosuggest").get_attribute('value') == 'India'
    CHROME_DRIVER.close()
