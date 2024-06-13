from dataclasses import dataclass


@dataclass
class VehicleData:
    category: str
    type_ts: str
    other_mark: str
    mark: str
    model: str
    year: str
    modification: str
    power: str
    purpose: str
    license_pate_number: str
    license_plate_region: str
    id_type: str
    id_value: str


@dataclass()
class VehicleEOsago_C:
    category: str = 'C - грузовые'
    type_ts: str = 'Грузовой а/м'
    other_mark: str = 'ДРУГОЕ ТС'
    mark: str = 'MERCEDES-BENZ'
    model: str = 'ARTEGO'
    year: str = '2019'
    modification: str = '170 л.с., Полный, АТ, Купе'
    power: str = '170'
    purpose: str = 'Личные'
    license_pate_number: str = 'О 172 ОА'
    license_plate_region: str = '799'
    id_type: str = 'VIN'
    id_value: str = 'WDC2539461F597886'
    weight: str = '10000'


@dataclass()
class VehicleEOsago_D:
    category: str = 'D - автобусы'
    type_ts: str = 'Автобусы'
    other_mark: str = 'ДРУГОЕ ТС'
    mark: str = 'MERCEDES-BENZ'
    model: str = 'CITARO'
    year: str = '2019'
    modification: str = '170 л.с., Полный, АТ, Купе'
    power: str = '170'
    purpose: str = 'Личные'
    license_pate_number: str = 'О 172 ОА'
    license_plate_region: str = '799'
    id_type: str = 'VIN'
    id_value: str = 'WDC2539461F597886'
    seats: str = '58'


@dataclass()
class VehicleEOsago_E:
    category: str = 'E - тракторы'
    type_ts: str = 'Трактора, самоходные и иные машины'
    other_mark: str = 'ДРУГОЕ ТС'
    mark: str = 'DAEWOO'
    model: str = 'F 3200'
    year: str = '2019'
    modification: str = '170 л.с., Полный, АТ, Купе'
    power: str = '170'
    purpose: str = 'Личные'
    license_pate_number: str = 'О 172 ОА'
    license_plate_region: str = '799'
    id_type: str = 'VIN'
    id_value: str = 'WDC2539461F597886'


@dataclass()
class VehicleEOsago_B:
    category: str = 'B - легковые'
    type_ts: str = 'Легковой а/м'
    other_mark: str = 'ДРУГОЕ ТС'
    mark: str = 'MERCEDES-BENZ'
    model: str = 'GLC-KLASSE'
    year: str = '2019'
    modification: str = '170 л.с., Полный, АТ, Купе'
    power: str = '170'
    purpose: str = 'Личные'
    license_pate_number: str = 'О 172 ОА'
    license_plate_region: str = '799'
    id_type: str = 'VIN'
    id_value: str = 'WDC2539461F597886'


@dataclass()
class VehicleEOsago_Ford:
    category: str = 'B - легковые'
    type_ts: str = 'Легковой а/м'
    other_mark: str = 'ДРУГОЕ ТС'
    mark: str = 'FORD'
    model: str = 'FOCUS'
    year: str = '2012'
    modification: str = '105 л.с., Передний, АТ, Седан'
    power: str = '105'
    purpose: str = 'Личные'
    license_pate_number: str = 'Н 725 ТВ'
    license_plate_region: str = '750'
    id_type: str = 'VIN'
    id_value: str = 'X9FMXXEEBMCG00639'
