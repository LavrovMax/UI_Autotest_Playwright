from dataclasses import dataclass


@dataclass()
class Address:
    zip_code: str = '107000'
    state: str = 'Москва'
    region = 'Москва'
    city: str = 'Москва'
    street: str = 'Петровка'
    house: str = '10'
    building: str = '4'
    apartment: str = '1'


@dataclass()
class Address_data:
    state: str = 'г Москва'
    region = 'г Москва'
    city: str = 'г Москва'
    street: str = 'ул Петровка'
    house: str = '10'
    building: str = '4'
    apartment: str = '1'


class Address_honda:
    zip_code: str = '141006'
    state: str = 'Московская область'
    region = 'Московская область'
    city: str = 'Мытищи'
    street: str = '3-я Пролетарская'
    house: str = '1'
    apartment: str = '1'
