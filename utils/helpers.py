from playwright.async_api import expect, Page


class Helper:

    def __init__(self, page):
        self.page = page

    def string_to_boolean(self, stringVal: str) -> bool:
        truthyValues = ('true', 'yes', '1', 'y')
        falsyValues = ('false', 'no', '0', 'n')
        stringVal = stringVal.strip().lower()
        if stringVal in truthyValues:
            return True
        elif stringVal in falsyValues:
            return False
        else:
            raise ValueError(f"Cannot convert {stringVal} to boolean")

    def validate_error_message_on_page(self, textMessage: str) ->bool:
        expect(self.page.get_by_text(textMessage)).to_be_visible()

    async def validate_heading_on_page(self, heading_text: str):
        await self.page.wait_for_load_state('domcontentloaded')

        try:
            heading = self.page.get_by_role('heading', name= heading_text)
            await heading.wait_for(state='visible', timeout=10000)
            await expect(heading).to_be_visible()
        except Exception as error:
            print(f'Heading "{heading_text}" not found. Check page content and selector.')
            raise  error

    def select_optionby_text_from_dropdown(self, element_locator:str, option: str):
        dropdown = self.page.locator(f'{element_locator}')
        dropdown.select_option(label=f'{option}')

    def convert_stringto_float(self, str_value: str, num_of_decimal_point = 2) -> float:
        return round(float(str_value),num_of_decimal_point)


