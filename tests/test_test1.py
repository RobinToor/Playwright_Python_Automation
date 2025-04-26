import json

from playwright.sync_api import Page


def test_11(page: Page):
    with open("../testData/credentials.json") as j:
        test_data = json.load(j)
        print(test_data)



    #page.goto("https://letstesttogether.com/store")