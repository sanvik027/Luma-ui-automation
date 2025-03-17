import pytest
from pages.registration_page import RegistrationPage
import softest
from ddt import ddt, data, unpack
from pages.dashboard_page import DashboardPage
from utilities.utility import Utils
@pytest.mark.usefixtures('setup')
@ddt
class TestValidLogin(softest.TestCase):
    log = Utils().custom_logger()

    @pytest.fixture(autouse=True)
    def setup_registration_page(self):
        self.reg_page = RegistrationPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)

    @data(*Utils.read_excel_data("C:\\Users\\chiranjibi\\PycharmProjects\\LumaShop\\testData\\user_data.xlsx", 'Sheet1'))
    @unpack
    def test_create_user_account(self,first_name,last_name,email,password,confirm_password):
        self.log.info("Testing Registration Page")
        self.reg_page.create_account(first_name, last_name, email, password,confirm_password)
        self.reg_page.verify_account_page_text("My Account")
        self.dashboard_page.log_out()

