from selenium import webdriver


# Web Drivers
# CHROME_DRIVER_EXECUTABLE_PATH = '/opt/selenium/chromedriver'
CHROME_DRIVER_EXECUTABLE_PATH = '/Users/bweber3/Downloads/chromedriver'
CHROME_DRIVER = webdriver.Chrome(executable_path=CHROME_DRIVER_EXECUTABLE_PATH)

# URLs
BRIANS_WEBSITE_URL = 'https://brianwweber.com'
SALESFORCE_LOGIN_URL = 'https://login.salesforce.com/'
RAHUL_SHETTY_URL = 'https://rahulshettyacademy.com'
