import logging
import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def set_implicit_wait(self,time_out=15):
        return self.driver.implicitly_wait(time_out)
    def page_scroll(self,time_out=2):
            pageLength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            match = False
            while (match == False):
                lastCount = pageLength
                time.sleep(time_out)
                pageLength = self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
                if lastCount == pageLength:
                    match = True
            time.sleep(time_out)

    def wait_for_presence_of_element(self,loc_type,locator):
        wait = WebDriverWait(self.driver,30)
        web_elements = wait.until(EC.presence_of_element_located((loc_type, locator)))
        return web_elements

    def get_page_title(self):
        return self.driver.title

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 30)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def click_with_retry(self,loc_type,locator,max_retries=3):

        for attempt in range(max_retries):
            try:
                element= self.wait_for_presence_of_element(loc_type,locator)
                element.click()
                logging.info("Clicked Successfully")
                break
            except StaleElementReferenceException:
                logging.warning(f"Attempt {attempt + 1} failed due to StaleElementReferenceException.")
                if attempt == max_retries-1:
                    logging.error("Max retries exceeded. Unable to click the element.")
                    raise #exception







