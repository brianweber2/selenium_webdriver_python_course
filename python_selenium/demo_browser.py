from selenium import webdriver

# Every browser exposes an executable file.
# Through Selenium test we need to invoke the executable file which will then invoke actual browser.
driver = webdriver.Chrome(executable_path='/opt/selenium/chromedriver')


if __name__ == '__main__':
    driver.maximize_window()
    driver.get('https://brianwweber.com')
    print(driver.title)
    print(driver.current_url)
    driver.get('https://brianwweber.com/my-story')
    driver.minimize_window()
    driver.back()
    driver.refresh()
    driver.close()
