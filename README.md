# Selenium Webdriver Python Course
My learnings on Selenium Python Automation from Basics to Advanced level + 5 LIVE Project.

## Setup
* Create virtualenv with Python3: `python3 -m venv venv`
* Activate virtualenv: `source venv/bin/activate`
* Install packages: `pip install -r requirements.lock`
* Download Selenium Chrome driver that matches the version of Chrome that you are using: https://sites.google.com/a/chromium.org/chromedriver/home
* Unzip the file and place in location `/opt/selenium/chromedriver`

## Running Tests

```
coverage run -m pytest --html=tests/report.html tests/
```

The tests report will be available in the **report.html** file that can be accessed via Chrome browser.

The output will also include a coverage report.
