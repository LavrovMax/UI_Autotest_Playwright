import pytest
from playwright.sync_api import expect
from pages.travel.shengen_insurence import InsuranceSchengenPage


class TestShengenInsurance:
    @pytest.mark.parametrize("device", ["desktop", "mobile"])
    def test_shengen_insurance(self, driver, device):
        insurens_page = InsuranceSchengenPage(driver, device)

        insurens_page.go_to('https://www.alfastrah.ru/individuals/travel/vzr/shengen/')

        # Заполнение информации
        insurens_page.choice_russia_and_china()
        insurens_page.begining_and_trip()
        insurens_page.participants_birthday()
        insurens_page.choice_type_recreation()

        # Нажатие на кнопку рассчитать
        insurens_page.calculate_cost()
        # page.close_pop_up()

        expect(insurens_page.locator.result()).to_be_visible()
        pass
