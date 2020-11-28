from config.config import CHROME_DRIVER_EXECUTABLE_PATH, BRIANS_WEBSITE_URL

from selenium import webdriver


if __name__ == '__main__':
    # Every browser exposes an executable file.
    # Through Selenium test we need to invoke the executable file which will then invoke actual browser.
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_EXECUTABLE_PATH)

    driver.maximize_window()
    driver.get(BRIANS_WEBSITE_URL)
    print(driver.title)
    print(driver.current_url)
    driver.get(f'{BRIANS_WEBSITE_URL}/my-story')
    driver.minimize_window()
    driver.back()
    driver.refresh()
    driver.close()
