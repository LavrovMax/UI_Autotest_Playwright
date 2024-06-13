from dataclasses import dataclass


@dataclass()
class Insurer:
    family: str = 'Тастов'
    name: str = 'Та ст'
    patronymic: str = 'Таст-ович'
    birthday: str = '02.03.1981'
    gender: str = 'Мужской'
    full_name: str = f'{family} {name} {patronymic}'
    pasport_series: str = '2222'
    pasport_number: str = '333333'
    pasport_date: str = '10.01.1991'
    inn: str = '123456789012'
    postal_address: str = '123456, Москва, Петровка, 1'
