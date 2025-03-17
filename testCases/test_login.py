
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

    @data(*Utils.read_excel_data("C:\\Users\\chiranjibi\\PycharmProjects\\LumaShop\\testData\\login_data.xlsx",'Sheet1'))
    @unpack
    def test_valid_login(self, email, password):
        self.log.info(f"Testing valid login with email: {email}")
        self.login_page.login(email, password)
        assert self.login_page.verify_homepage_text('Home Page'), "Homepage text verification failed!"
        self.dashboard_page.log_out()
        self.log.info("✅ Valid login executed successfully.")

    def test_invalid_login(self):
        self.login_page.login("invalid_login @gmail.com","Demo@123")
        self.login_page.verify_login("Customer Login")
        self.log.info("Invalid login executed")





