from pages.travel.base_page import BasePage
from locators.travel.insurance_schengen_locators import InsuranceSchengenLocators


class InsuranceSchengenPage(BasePage):
    def __init__(self, page, device):
        super().__init__(page)
        self.device = device
        self.locator = InsuranceSchengenLocators(self.page, self.device)

    def choice_russia_and_china(self):
        self.locator.russia.click()
        self.locator.specify_country.fill('Китай')
        self.page.keyboard.press('Enter')

    def begining_and_trip(self):
        self.locator.beginning_policy.fill('30.04.2024')
        self.locator.end_policy.fill('30.03.2025')

    def participants_birthday(self):
        self.locator.birthday_first.fill('13.07.1995')
        self.locator.crutch.click()
        self.locator.add_participant.click()
        self.locator.birthday_second.fill('02.03.1981')
        self.locator.crutch.click()

    def choice_type_recreation(self):
        self.locator.input_sport.fill("треккинг")
        self.page.keyboard.press('Enter')
        # self.locator.trekking.click()
        self.locator.list_sport.click()
        self.locator.scrolling.click()
        self.press_page_down_multiply(3, "PageDown")
        # self.page.keyboard.press('PageDown')
        # self.page.keyboard.press('PageDown')
        # self.page.keyboard.press('PageDown')
        self.locator.yachting.click()
        # self.page.mouse.wheel(300, 300)
        # self.locator.yachting.click()
        self.locator.btn_select_and_close.click()

    def calculate_cost(self):
        self.locator.btn_calculate_cost.click()

    # def close_pop_up(self):
    #     self.locator.pop_up.click()

    def checking_result(self):
        return self.locator.result()



