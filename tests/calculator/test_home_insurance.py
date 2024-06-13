import pytest
from pages.calculator.home_insurance import HomeInsurance
from playwright.sync_api import expect
from test_data.document import Passport
from test_data.contact import Contact
from test_data.insurer import Insurer
from test_data.address import Address
import time


class TestHomeInsurance:
    @pytest.mark.parametrize("device", ["desktop", "mobile"])
    def test_home_insurance(self, driver, device):
        page = HomeInsurance(driver, device)

        page.go_to("https://www.alfastrah.ru/individuals/housing/flat/members/")

        # Выбор программы страхования
        page.program_selection()

        # Заполнение контактной информации
        page.contact_info(contact=Contact())
        page.insurer(insurer=Insurer())
        page.passport(passport=Passport())

        # Заполнение информации о объекте страхования
        page.address_insurance(address=Address())

        # Начало срока страхования и согласие на обработку персональных данных
        page.policy_data()
        page.agreement()

        page.btn_go_to_payments()

        expect(page.locator.result).to_be_visible()
