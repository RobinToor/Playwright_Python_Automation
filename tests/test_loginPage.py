import json
import pytest
import os
from playwright.sync_api import Page, expect, Playwright
from pageObjects.loginPage import LoginPage

file_path = os.path.join(os.path.dirname(__file__), '..', 'testData', 'credentials.json')
file_path = os.path.abspath(file_path)

with open(file_path) as j:
    test_data = json.load(j)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.parametrize('login_details', user_credentials_list)
def test_loginToTheStoreWebsite(playwright: Playwright, browserInstance, login_details):
    page = browserInstance
    username = login_details['username']
    password = login_details['password']

    #object of loginPage class
    loginPage = LoginPage(page)
    loginPage.navigate()
    loginPage.login(username, password)

    #assert
    expect(page.get_by_role("heading", name="My Account")).to_be_visible()
