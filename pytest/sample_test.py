# to run this, just: pytest -> https://playwright.dev/python/docs/test-runners
# pytest --headed
# pytest --browser chromium --browser webkit
# pytest --browser-channel chrome --headed
# pytest --base-url https://www.saucedemo.com/ --browser chromium --headed
# Run tests with slow mo with the --slowmo argument.: --slowmo 1000


# Configure Mypy typings for auto-completion
from playwright.sync_api import Page

import pytest


# --Skip test by browser
# @pytest.mark.skip_browser("firefox")
# --Run on a specific browser
# @pytest.mark.only_browser("chromium")
def test_title(page: Page):
    page.goto("/")
    assert page.inner_text("title") == "Swag Labs"


def test_inventory_site(page: Page):
    page.goto("/inventory.html")
    assert (
        page.inner_text("h3")
        == "Epic sadface: You can only access '/inventory.html' when you are logged in."
    )
