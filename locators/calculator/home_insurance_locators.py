from playwright_framework.locators.сustom_locators import CustomLocator
from pages.calculator.base_page import BasePage


# https://www.alfastrah.ru/individuals/housing/flat/members/


class HomeInsuranceLocators(BasePage):
    def __init__(self, page, device):
        super().__init__(page)
        self.device = device

    @property
    def program_one(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//button[@type="submit"])[2]'), "выбор програмы")

    @property
    def email(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#email'), "емейл")

    @property
    def phone(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#tel'), "телефон")

    @property
    def surname(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#last_name'), "фамилия")

    @property
    def name(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#first_name'), "имя")

    @property
    def patronymic(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#middle_name'), "отчество")

    @property
    def birthday(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#birthday'), "дата рождения")

    @property
    def crutch(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//h2)[1]'), "костыль чтоб закрыть календарь")

    @property
    def gender(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//span[text()="Мужской"]'), "пол")

    @property
    def passport_series(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#passport-serial'), "серия паспорта")

    @property
    def passport_numbers(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#passport-number'), "номер паспорта")

    @property
    def passport_issue(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#issue'), "дата выдачи")

    @property
    def city(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#js-step2-form-city'), "город")

    @property
    def second_item_list(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//div[@class="suggestions-suggestion"][2]'), "город")

    @property
    def street(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//input[@placeholder="Улица"]'), "улица")

    @property
    def house(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//input[@placeholder="Дом"]'), "дом")

    @property
    def building(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//input[@placeholder="Строение / корпус"]'), "строение")

    @property
    def flat(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//input[@placeholder="Квартира"]'), "квартира")

    @property
    def policy_date(self) -> CustomLocator:
        return CustomLocator(self.page.locator('#insurance-start'), "начало срока страхования")

    @property
    def agreement_1(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//span[@class="checkbox__symbol"]'), "чекбокс согласия")

    @property
    def btn_arrange(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//button[@class="btn js-submit"]'), "кнопка оформить")

    @property
    def result(self):
        return self.page.locator('//h2[text()="Выберите способ оплаты"]')
