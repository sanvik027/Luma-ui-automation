
import pytest
import softest
from ddt import ddt, data, unpack
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utilities.utility import Utils


@pytest.mark.usefixtures('setup')
@ddt
class TestValidLogin(softest.TestCase):
    log = Utils().custom_logger()


    @pytest.fixture(autouse=True)
    def setup_login_page(self):
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)

    @data(*Utils.read_excel_data("C:\\Users\\chiranjibi\\PycharmProjects\\LumaShop\\testData\\login_data.xlsx", 'Sheet1'))
    @unpack
    @pytest.mark.order(2)
    def test_login(self, email, password, expected_result):
        """
        Unified method to handle both valid and invalid login tests.
        :param email: Email used for login
        :param password: Password used for login
        :param expected_result: 'valid' or 'invalid' to specify expected outcome
        """
        self.log.info(f"Testing login with email: {email}, expected result: {expected_result}")

        # Perform login
        self.login_page.login(email, password)

        # Conditional logic based on expected result
        if expected_result == "valid":
            assert self.login_page.verify_homepage_text('Home Page'), "Homepage text verification failed!"
            self.dashboard_page.log_out()
            self.log.info("Valid login executed successfully.")
            self.dashboard_page.log_out()
        elif expected_result == "invalid":
            assert self.login_page.verify_login("Customer Login"), "Invalid login verification failed!"
            self.log.info("Invalid login executed successfully.")
        else:
            self.log.error("Unexpected result type in test data.")




