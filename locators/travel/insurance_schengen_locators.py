from playwright_framework.locators.сustom_locators import CustomLocator
from pages.travel.base_page import BasePage


class InsuranceSchengenLocators(BasePage):
    def __init__(self, page, device):
        super().__init__(page)
        self.device = device

    @property
    def russia(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//a[@class="link--dotted link--gray js-vzr-country-fast-select"])[2]'),
                             "выбор России в списке")

    @property
    def specify_country(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//input[@role="textbox"])[1]'), "полу ввода страны")

    # def china(self) -> CustomLocator:
    #     return CustomLocator(self.page.locator(''), "")

    @property
    def beginning_policy(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//input[@placeholder="__.__.____"])[1]'),
                             "начало действия полиса")

    @property
    def end_policy(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//input[@placeholder="__.__.____"])[2]'),
                             "окончание действия локатора")

    @property
    def birthday_first(self) -> CustomLocator:
        return CustomLocator(self.page.locator(
            '(//div[@class="numbered-fields__item js-vzr-person"]/div/div/input)[1]'),
                             "день рождения первого участника")

    @property
    def add_participant(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//a[@class="link link--dotted link--add"]'),
                             "добавить участника")

    @property
    def birthday_second(self) -> CustomLocator:
        return CustomLocator(self.page.locator(
            '(//div[@class="numbered-fields__item js-vzr-person"]/div/div/input)[2]'),
                             "день рождения второго участника")

    @property
    def crutch(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//h1[text()="Медицинская страховка для Шенгенской визы"]'),
                             "клик чтоб закрыть календарь")

    @property
    def list_sport(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//a[@class="link link--dotted link--ico-list"]'),
                             "список видов спорта")

    @property
    def yachting(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//span[@class="categories__option categories__option--underline"])[84]'),
                             "Яхтинг")

    @property
    def btn_select_and_close(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//button[@class="btn btn--middle js-submit-select-list"]'),
                             "выбрать и закрыть")

    @property
    def input_sport(self) -> CustomLocator:
        return CustomLocator(self.page.locator('(//input[@role="textbox"])[2]'),
                             "поле ввода видов спорта")

    @property
    def scrolling(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//div[@class="scrollbar-track scrollbar-track-y show"]'),
                             "скроллинг")

    @property
    def trekking(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//li[@id="select2-vzr-sport-91-result-63x0-71"]'),
                             'треккинг в выпадающем окне')

    @property
    def btn_calculate_cost(self) -> CustomLocator:
        return CustomLocator(self.page.locator('//button[@class="btn btn-lg js-vzr-submit-button"]'))

    # @property
    # def pop_up(self):
    #     return self.page.locator('//button[@class="PushTip-buttonItem"]')

    def result(self) -> CustomLocator:
        return CustomLocator(self.page.locator(
            '//button/span[@class="i-button__text" and text()="Пересчитать стоимость"]'))

