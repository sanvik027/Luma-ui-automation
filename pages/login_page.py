import logging
from selenium.webdriver.common.by import By
from utilities.utility import Utils
from base.base_driver import BaseDriver


class LoginPage(BaseDriver):
    log = Utils().custom_logger(log_level=logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    SIGIN_LINK = "(//a[normalize-space()='Sign In'])[1]"
    CUSTOMER_EMAIL = "email"
    CUSTOMER_PASSWORD = "pass"
    LOGIN_BTN = "send2"
    WELCOME_TXT = "(//span[contains(text(),'Chiranjibi')])[1]"
    HOME_PAGE_TXT = "//h1"

    def navigate_signin(self):
        return self.wait_for_presence_of_element(By.XPATH,self.SIGIN_LINK)

    def get_cust_email(self):
        return self.wait_until_element_is_clickable(By.ID,self.CUSTOMER_EMAIL)

    def get_cust_password(self):
        return self.wait_until_element_is_clickable(By.ID,self.CUSTOMER_PASSWORD)

    def get_login_btn(self):
        return self.wait_until_element_is_clickable(By.ID,self.LOGIN_BTN)

    #def get_welcome_text(self):
       # return self.wait_for_presence_of_element(By.XPATH,self.WELCOME_TXT)

    def get_home_page_text(self):
        return self.wait_for_presence_of_element(By.XPATH,self.HOME_PAGE_TXT).text

    def enter_email(self,email):
      self.get_cust_email().send_keys(email)

    def enter_password(self,password):
        self.get_cust_password().send_keys(password)

    def click_login_btn(self):
        self.get_login_btn().click()

    def login(self,email,password):
        self.navigate_signin().click()
        self.enter_email(email)
        self.enter_password(password)
        self.page_scroll()
        self.click_login_btn()
        self.log.info("Logging Successful")

    def verify_login(self, expected_title):
        page_title = self.get_page_title()
        assert page_title == expected_title
        self.log.info("Page title mathced in case of invalid Credentials")

    def verify_homepage_text(self,expected_text):
        homepage_text = self.get_home_page_text()
        assert homepage_text == expected_text
        self.log.info("Header text verified in case of valid credentials")




