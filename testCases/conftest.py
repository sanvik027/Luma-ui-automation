"""
Common Configuration file
"""
import pytest
from selenium import  webdriver
@pytest.fixture(scope='function',autouse=True)
def setup(request, browser,url):
    global driver

    # Convert browser name to lowercase for case-insensitive matching
    browser_lower = browser.lower()
    if browser_lower == "chrome":
        driver = webdriver.Chrome()
    elif browser_lower == "firefox":
        driver = webdriver.Firefox()
    elif browser_lower == "edge":
        driver = webdriver.Edge()
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="function", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="function", autouse=True)
def url(request):
    return request.config.getoption("--url")


