from playwright.sync_api import expect, Page

from utils.helpers import Helper


class SubscribePage:

    def __init__(self, page):
        self.page = page

    def fillInfoToSubscribe(self, firstName, lastName, emailAddress,isCaptchaValid):
        self.page.get_by_role("button", name="Subscribe").click()
        self.page.get_by_role("textbox", name="First Name:").fill(firstName)
        self.page.get_by_role("textbox", name="Last Name:").fill(lastName)
        self.page.get_by_role("textbox", name="E-Mail:").fill(emailAddress)
        helper = Helper(self.page)
        isvalid = helper.string_to_boolean(isCaptchaValid)
        if not isvalid:
            self.page.get_by_role("textbox", name="Enter code:").fill("h34vhj")
        else:
            print("need to implement code to get Captcha value")
        self.page.get_by_role("button", name=" Continue").click()



