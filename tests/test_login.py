import pytest
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
class TestLogin:

    
    def test_successful_login(self, page):
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory" in page.url
    
    @pytest.mark.regression
    def test_invalid_login(self, page):
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("standard_user", "wrong_password")

        assert login_page.is_error_displayed()
        assert login_page.get_error_message() == \
"Epic sadface: Username and password do not match any user in this service"
        