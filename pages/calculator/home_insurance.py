import allure

from pages.calculator.base_page import BasePage
from locators.calculator.home_insurance_locators import HomeInsuranceLocators
from test_data.document import Passport
from test_data.contact import Contact
from test_data.insurer import Insurer
from test_data.address import Address


class HomeInsurance(BasePage):
    def __init__(self, page, device):
        super().__init__(page)
        self.device = device
        self.locator = HomeInsuranceLocators(self.page, self.device)
        self.contact = Contact()

    @allure.step('выбираем програму')
    def program_selection(self):
        self.locator.program_one.click()

    @allure.step("заполняем контакртные данные")
    def contact_info(self, contact: Contact):
        self.locator.email.fill(value=contact.email)
        self.locator.phone.fill(value=contact.phone)

    @allure.step("заполняем данные пользователя")
    def insurer(self, insurer: Insurer):
        self.locator.surname.fill(value=insurer.family)
        self.locator.name.fill(value=insurer.name)
        self.locator.patronymic.fill(value=insurer.patronymic)
        self.locator.birthday.fill(value=insurer.birthday)
        self.locator.crutch.click()
        self.locator.gender.click()

    @allure.step("заполняем паспортные данные")
    def passport(self, passport: Passport):
        self.locator.passport_series.fill(value=passport.serial)
        self.locator.passport_numbers.fill(value=passport.number)
        self.locator.passport_issue.fill(value=passport.issue_date)
        self.locator.crutch.click()

    @allure.step("заполняем информацию о адресе страхуемой недвижемости")
    def address_insurance(self, address: Address):
        self.locator.city.fill(value=address.city)
        self.locator.second_item_list.click()
        self.locator.street.fill(value=address.street)
        self.locator.house.fill(value=address.house)
        self.locator.building.fill(value=address.building)
        self.locator.flat.fill(value=address.apartment)

    def policy_data(self):
        self.locator.policy_date.fill("15.06.2024")
        self.locator.crutch.click()

    def agreement(self):
        # self.locator.agreement_1.focus()
        # self.page.keyboard.press("Space")
        self.locator.agreement_1.click()

    def btn_go_to_payments(self):
        self.locator.btn_arrange.click()
