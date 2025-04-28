from playwright.sync_api import Playwright, expect
from  pageObjects.subscribePage import SubscribePage
from pageObjects.loginPage import LoginPage
from utils.Constants import AppConstants
from utils.helpers import Helper

def test_subscribeWithInvalidValid(playwright: Playwright, browserInstance):
    page = browserInstance
    loginPage = LoginPage(page)
    loginPage.navigate()
    subscribePage = SubscribePage(page)
    subscribePage.fillInfoToSubscribe(firstName="Raven",lastName="Bond", emailAddress="xyz@email.com", isCaptchaValid="no")
    appconstants = AppConstants()
    helper = Helper(page)
   # helper.validate_error_message_on_page("Human verification has failed! Please try agan.")
