import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utility import Utils


class RegistrationPage(BaseDriver):
    log = Utils().custom_logger(log_level=logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    CREATE_ACCOUNT = 'Create an Account'
    FIRST_NAME = 'firstname'
    LAST_NAME = 'lastname'
    EMAIL = 'email_address'
    PASSWORD = 'password'
    CONFIRM_PASSWORD = 'password-confirmation'
    CREATE_ACCOUNT_BTN = "//button[@title='Create an Account']"
    CUSTOMER_ACCOUNT_TEXT ="//h1"

    def navigate_to_create_account(self):
        return self.wait_until_element_is_clickable(By.PARTIAL_LINK_TEXT,self.CREATE_ACCOUNT)

    def get_first_name(self):
        return self.wait_for_presence_of_element(By.ID,self.FIRST_NAME)

    def get_last_name(self):
       return self.wait_for_presence_of_element(By.ID,self.LAST_NAME)

    def get_email(self):
       return self.wait_for_presence_of_element(By.ID,self.EMAIL)

    def get_password(self):
       return self.wait_for_presence_of_element(By.ID,self.PASSWORD)

    def get_confirm_password(self):
        return self.wait_for_presence_of_element(By.ID,self.CONFIRM_PASSWORD)

    def get_create_account_btn(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.CREATE_ACCOUNT_BTN)
    def click_create_accnt_link(self):
        return self.navigate_to_create_account().click()

    def enter_first_name(self,name):
        self.get_first_name().send_keys(name)

    def enter_last_name(self,last_name):
        self.get_last_name().send_keys(last_name)

    def enter_email(self,email):
        self.get_email().send_keys(email)

    def enter_password(self,password):
        self.get_password().send_keys(password)

    def enter_confirm_password(self,confirm_password):
        self.get_confirm_password().send_keys(confirm_password)

    def click_create_account_btn(self):
        self.get_create_account_btn().click()

    def get_account_page_text(self):
        return self.wait_for_presence_of_element(By.XPATH,self.CUSTOMER_ACCOUNT_TEXT)

    def create_account(self,first_name,last_name,email,password,confirm_password):
        self.click_create_accnt_link()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.click_create_account_btn()

    def verify_account_page_text(self, expected_text):
        accnt_page_text = self.get_account_page_text().text
        Utils.verify_text(accnt_page_text, expected_text, self.log, "Homepage header text verified successfully")






