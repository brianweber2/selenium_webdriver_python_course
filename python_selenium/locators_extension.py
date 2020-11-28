from config.config import DRIVER, SALESFORCE_LOGIN_URL


if __name__ == '__main__':
    DRIVER.get(SALESFORCE_LOGIN_URL)
    DRIVER.find_element_by_css_selector('#username').send_keys('Brian')
    DRIVER.find_element_by_css_selector('.password').send_keys('test1234')
    DRIVER.find_element_by_css_selector('.password').clear()
    DRIVER.find_element_by_link_text('Forgot Your Password?').click()
    DRIVER.find_element_by_xpath("//a[text()='Cancel']").click()
    DRIVER.find_element_by_xpath("//form[@name='login']/div[1]/label")
    DRIVER.close()
