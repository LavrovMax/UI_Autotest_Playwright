from playwright_framework.locators.сustom_locators import CustomLocator
from pages.osago.base_page import BasePage


class InsuranseOsagoLocators(BasePage):
    def __init__(self, page, devise):
        super().__init__(page)
        self.devise = devise

    @property
    def banner_one(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//button[@class="PushTip-buttonItem"]'),
                             "Закрываем баннер")

    @property
    def banner_two(self) -> CustomLocator:
        return CustomLocator(self.page.frame_locator('#fl-750975').locator('//button[@class="widget__close"]'),
                             "Закрываем еще один баннер")

    @property
    def consent_cookies(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//span[@id="closeCookieInfo"]'),
                             "соглашаемся с куками")

    @property
    def not_registered(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//label[@class="checkbox__label"])[1]'),
                             "проставляем чекбокс не поставлена на учет")

    @property
    def transport_id(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//span[@id="select2-CarIdType-container"]'),
                             "Список идентификаторов транспорта")

    @property
    def select_transport_id(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//li[text()="Номер кузова"]'),
                             "Поле ввода для идентификатора")

    @property
    def body_number(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//input[@placeholder="Введите номер кузова"]'),
                             "Поле для ввода номера кузова")

    @property
    def transport_category(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//span[@id="select2-category-container"]'),
                             "Категория транспорта")

    @property
    def passenger_transport_b(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//li[text()="B - легковые"]'),
                             "Тип транспорта B")

    @property
    def passenger_transport_c(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//li[text()="C - грузовые"]'),
                             "Тип транспорта С")

    @property
    def passenger_transport_d(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//li[text()="D - автобусы"]'),
                             "Тип транспорта D")

    @property
    def passenger_transport_e(self) -> CustomLocator:
        return (CustomLocator(self.page.locator('//li[text()="E - тракторы"]'),
                             "Тип транспорта E"))

    def passenger_transport(self, category) -> CustomLocator:
        return CustomLocator(self.page.locator(f'//li[text()="{category}"]'),
                             f"Тип транспорта {category}")

    @property
    def mark_transport(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//input[@id="mark"]'),
                             "Марка транспорта")

    @property
    def model_transport(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//input[@id="model"]'),
                             "Поле для ввода модели транспорта")

    @property
    def model_125(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//div[text()="125"]'),
                             "Конкретная модель")

    @property
    def year_release(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//input[@id="year"]'),
                             "Год выпуска")

    @property
    def modification(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//label[@for="modification"]/parent::div/span'),
                             "Список модификаций")

    @property
    def modification_type(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//li[contains(@id,"select2-modification-result")])[1]'),
                             "Конкретная модификация")

    # @property
    # def power(self) -> CustomLocator:
    #     return CustomLocator(self.page.locator('//input[@id="carPower"]'))

    @property
    def purpose_use(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//span[@class="input js-input js-input--with-scrollbar"])[2]'),
                             "Список целей использования")

    @property
    def purpose_rent(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//li[contains(@id,"select2-purposeName")])[5]'),
                             'Цель использования')

    @property
    def for_rent(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//label[@for="rent"]'), "Чекбокс сдаётся в аренду")

    @property
    def current_policy_osago_series(self):
        if 'desktop' in self.devise:
            return self.page.locator('(//span[@class="select2-selection select2-selection--single"])[6]')
        elif 'mobile' in self.devise:
            return None

    @property
    def choise_osago_series(self):
        if 'desktop' in self.devise:
            return self.page.locator('(//li[contains(@id, "select2-currentPolicySerial")])[3]')
        elif 'mobile' in self.devise:
            return None

    @property
    def current_policy_osago_number(self):
        if 'desktop' in self.devise:
            return self.page.locator('//input[@class="input__control page-calculator-osago__input-control"]')
        elif 'mobile' in self.devise:
            return None

    @property
    def btn_further(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//button[@class="btn js-submit-osago-step-1"]'),
                             "Кнопка далее")

    @property
    def max_weight(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//input[@id="Weight"]'),
                             "Разрешенная максимальная масса")

    @property
    def passenger_seats(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//input[@id="Seats"]'),
                             "Количество пассажирских мест")

    @property
    def next_page(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//h1[text()="Электронное ОСАГО"]'), "Следующая страница")
