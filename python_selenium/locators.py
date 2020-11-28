import time

from config.config import BRIANS_WEBSITE_URL, DRIVER

from selenium import webdriver


# https://autonomiq.io/chropath/


if __name__ == '__main__':
    DRIVER.get(f'{BRIANS_WEBSITE_URL}/contact')

    # Fill out form details.
    DRIVER.find_element_by_name('fname').send_keys('Brian')
    DRIVER.find_element_by_name('lname').send_keys('Weber')
    DRIVER.find_element_by_name('email').send_keys('test@gmail.com')
    DRIVER.find_element_by_xpath("//*[@id='text-yui_3_17_2_1_1458369982168_127478-field']").send_keys('Selenium Test')
    DRIVER.find_element_by_css_selector("#textarea-yui_3_17_2_1_1458369982168_127906-field").send_keys('This is a '
                                                                                                       'test from '
                                                                                                       'Selenium.')

    # Send Email
    # driver.find_element_by_id('').click()
    # driver.find_element_by_css_selector("input[type='submit']").click()  # "tagname[attribute='value']"
    DRIVER.find_element_by_xpath("//input[@type='submit']").click()  # "//tagname[@attribute='value']"

    time.sleep(2)  # To allow for page to load after email is sent.

    # Reg ex: //*[attribute*='value'] or //*[contains(@class,'value')]
    print(DRIVER.find_element_by_xpath("//div[@class='form-submission-text']/p").text)

    DRIVER.close()
