from playwright.sync_api import Page, expect
from utils.helpers import Helper

class ProductInfo:

    def __init__(self, page:Page):
        self.page = page
        self.plus_quantity = page.locator(".plus-qnty")
        self.minus_quantity = page.locator(".minus-qnty")
        self.product_quantity = page.locator("#product_quantity")
        self.total_price = page.locator(".total-price")
        self.model_number = page.locator("//span[.='Model:']")
        self.product_price = page.locator(".text-danger.mb-0")

    def updateQuantity(self, quantity):
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        required_qty = int(quantity)
        default_qty = 1
        if required_qty > default_qty:
            for x in range(required_qty - default_qty):
                initial_value = self.product_price.text_content()
                self.plus_quantity.wait_for(state="visible")
                self.plus_quantity.click()
                self.page.expect_response(
                    lambda response: "/store/index.php?rt=r/product/product/calculateTotal" in response.url and response.status == 200)

                self.page.wait_for_timeout(2500)

                self.page.wait_for_function(
                    """(initial_value) => {
                        const totalPriceElement = document.querySelector('.total-price');
                        return totalPriceElement && totalPriceElement.textContent !== initial_value;
                    }""",
                    arg=initial_value
                )

    def verify_total_price(self, required_qty):
        self.page.wait_for_load_state('domcontentloaded')
        price_of_product =self.product_price.text_content()
        helper = Helper(self.page)
        price_of_product = helper.convert_stringto_float(price_of_product)
        expected_price =  price_of_product * float(required_qty)
        expected_price = helper.convert_stringto_float(expected_price,2)
        actual_total_price = helper.convert_stringto_float(self.total_price.text_content())

        expect(actual_total_price).toBe(expected_price)