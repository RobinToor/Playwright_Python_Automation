from playwright.sync_api import expect


class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://letstesttogether.com/store")

    def login(self, username, password):
        self.page.get_by_title("Login").click()
        expect(self.page.get_by_role("heading", name="Account Login")).to_be_visible()
        self.page.locator("#loginFrm_loginname").fill(username)
        self.page.locator("#loginFrm_password").fill(password)
        self.page.get_by_role("button", name=" Login").click()
