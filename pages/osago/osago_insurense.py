from pages.osago.base_page import BasePage
from locators.osago.insuranse_osago_locators import InsuranseOsagoLocators
from test_data.vehicle import VehicleEOsago_B, VehicleEOsago_C, VehicleEOsago_Ford, VehicleEOsago_E, VehicleEOsago_D
# https://www.alfastrah.ru/individuals/auto/eosago/calc/


class OsagoInsuransePage(BasePage):
    def __init__(self, page, device):
        super().__init__(page)
        self.device = device
        self.locator = InsuranseOsagoLocators(self.page, self.device)

    def close_banners_and_cookies(self):
        self.locator.banner_two.click()
        self.locator.consent_cookies.click()

    def check_not_registered_transport(self):
        self.locator.not_registered.check()

    def filling_data_transport(self, vehicle_data):
        self.locator.transport_id.click()
        self.locator.select_transport_id.click()
        self.locator.body_number.fill(vehicle_data.id_value)
        self.locator.transport_category.click()
        self.locator.passenger_transport(vehicle_data.category).click()
        # if vehicle_data.category == "C - грузовые":
        #     self.locator.passenger_transport_c.click()
        # elif vehicle_data.category == "D - автобусы":
        #     self.locator.passenger_transport_d.click()
        # elif vehicle_data.category == "B - легковые":
        #     self.locator.passenger_transport_b.click()
        # elif vehicle_data.category == 'E - тракторы':
        #     self.locator.passenger_transport_e.click()
        # else:
        # pass

        self.locator.mark_transport.fill(vehicle_data.mark)
        self.locator.model_transport.fill(vehicle_data.model)
        self.locator.year_release.fill(vehicle_data.year)

    def choosing_modification(self, vehicle_data):
        if vehicle_data.category == "B - легковые":
            self.locator.modification.click()
            self.locator.modification.click()
            self.locator.modification_type.click()

        elif vehicle_data.category == "C - грузовые":
            self.locator.max_weight.fill(vehicle_data.weight)

        elif vehicle_data.category == "D - автобусы":
            self.locator.passenger_seats.fill(vehicle_data.seats)

    def purposes_use(self):
        self.locator.purpose_use.click()
        self.locator.purpose_rent.click()
        self.locator.for_rent.check()

    def current_policy(self):
        if self.device == 'desktop':
            self.locator.current_policy_osago_series.click()
            self.locator.choise_osago_series.click()
            self.locator.current_policy_osago_number.fill('0107747778')
        elif self.device == 'mobile':
            pass

    def btn_further(self):
        self.locator.btn_further.click()
        