from selenium import webdriver


CHROME_DRIVER_EXECUTABLE_PATH = '/opt/selenium/chromedriver'
BRIANS_WEBSITE_URL = 'https://brianwweber.com'
SALESFORCE_LOGIN_URL = 'https://login.salesforce.com/'
DRIVER = webdriver.Chrome(executable_path=CHROME_DRIVER_EXECUTABLE_PATH)
