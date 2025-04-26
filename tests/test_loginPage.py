import json
import pytest
from playwright.sync_api import Page, expect, Playwright
from pytest_playwright.pytest_playwright import browser, new_context
from pageObjects.loginPage import LoginPage

with open("../testData/credentials.json") as j:
    test_data = json.load(j)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.parametrize('login_details', user_credentials_list)
def test_loginToTheStoreWebsite(playwright: Playwright, login_details):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    username = login_details['username']
    password = login_details['password']

    #object of loginPage class
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.login(username, password)

    #assert
    expect(page.get_by_role("heading", name="My Account")).to_be_visible()

    # closing browser
    context.close()
    browser.close()

