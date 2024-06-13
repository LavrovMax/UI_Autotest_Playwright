import pytest
from pages.osago.osago_insurense import OsagoInsuransePage
from test_data.vehicle import VehicleEOsago_B
from test_data.vehicle import VehicleEOsago_C
from test_data.vehicle import VehicleEOsago_E
from test_data.vehicle import VehicleEOsago_D
from test_data.vehicle import VehicleEOsago_Ford
from playwright.sync_api import expect


class TestOsagoInsurance:
    @pytest.mark.parametrize("vehicle_data",
                             [VehicleEOsago_B(), VehicleEOsago_C(), VehicleEOsago_D(), VehicleEOsago_E()])
    def test_osago_insurence_b(self, driver, vehicle_data):
        page_osago_insuranse = OsagoInsuransePage(driver, device="desktop")
        # vehicle_data = VehicleEOsago_B()

        page_osago_insuranse.go_to('https://www.alfastrah.ru/individuals/auto/eosago/calc/')
        page_osago_insuranse.close_banners_and_cookies()

        # Заполнение информации о транспорте
        page_osago_insuranse.check_not_registered_transport()
        page_osago_insuranse.filling_data_transport(vehicle_data)
        page_osago_insuranse.choosing_modification(vehicle_data)
        page_osago_insuranse.purposes_use()

        # Заполнение информации о текущем полисе
        page_osago_insuranse.current_policy()
        page_osago_insuranse.btn_further()

        expect(page_osago_insuranse.locator.next_page).to_be_visible()
        pass



