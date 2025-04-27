import pytest
import os
import sys
from playwright.sync_api import Page, Playwright


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="Input browser of your choice"
    )
    parser.addoption(
        "--url_name", action="store", default="https://letstesttogether.com/store", help="Input server Url"
    )


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


@pytest.fixture
def browserInstance(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    url_name = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    #page.goto(url_name)
    yield page
    context.close()
    browser.close()
