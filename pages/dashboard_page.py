import logging

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utility import Utils


class DashboardPage(BaseDriver):
    log = Utils().custom_logger(log_level=logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    # Locators
    WELCOME_HOVER ="//div[@class='panel header']//button[@type='button']"
    SIGN_OUT_LINK = "(//li/a[contains(.,'Sign Out')])[1]"

    def move_welcome_text(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.WELCOME_HOVER)
    def get_sign_out_link(self):
        return self.wait_until_element_is_clickable(By.XPATH,self.SIGN_OUT_LINK)

    def log_out(self):
        self.move_welcome_text().click()
        self.get_sign_out_link().click()
        self.log.info("Logout Successful")



