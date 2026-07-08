import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
@pytest.mark.regression
class TestInventory:

    def test_verify_inventory_page_after_login(self, page):

        # Login
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login(
            "standard_user",
            "secret_sauce"
        )

        # Verify inventory page
        inventory_page = InventoryPage(page)

        assert inventory_page.get_page_title() == "Products"

    def test_verify_products_are_displayed(self, page):

        # Login
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login(
            "standard_user",
            "secret_sauce"
        )

        # Verify products
        inventory_page = InventoryPage(page)

        assert inventory_page.get_product_count() > 0