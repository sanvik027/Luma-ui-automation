
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

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



