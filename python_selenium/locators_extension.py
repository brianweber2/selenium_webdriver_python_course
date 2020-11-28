from config.config import CHROME_DRIVER, SALESFORCE_LOGIN_URL


if __name__ == '__main__':
    CHROME_DRIVER.get(SALESFORCE_LOGIN_URL)
    CHROME_DRIVER.find_element_by_css_selector('#username').send_keys('Brian')
    CHROME_DRIVER.find_element_by_css_selector('.password').send_keys('test1234')
    CHROME_DRIVER.find_element_by_css_selector('.password').clear()
    CHROME_DRIVER.find_element_by_link_text('Forgot Your Password?').click()
    CHROME_DRIVER.find_element_by_xpath("//a[text()='Cancel']").click()
    print(CHROME_DRIVER.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
    print(CHROME_DRIVER.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)
    CHROME_DRIVER.close()
