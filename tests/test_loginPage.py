import json
import pytest
from playwright.sync_api import Page, expect, Playwright
from pytest_playwright.pytest_playwright import browser, new_context

with open("../testData/credentials.json") as j:
    test_data = json.load(j)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.parametrize('login_details', user_credentials_list)
def test_login_tothestorewebsite(playwright: Playwright, login_details):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://letstesttogether.com/store")
    page.get_by_title("Login").click()
    expect(page.get_by_role("heading", name="Account Login")).to_be_visible()
    page.locator("#loginFrm_loginname").fill(login_details['username'])
    page.locator("#loginFrm_password").fill(login_details['password'])
    page.get_by_role("button", name=" Login").click()
    expect(page.get_by_role("heading", name="My Account")).to_be_visible()
    # closing browser
    context.close()
    browser.close()


