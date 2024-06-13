from dataclasses import dataclass


@dataclass
class Contact:
    email: str = 'test_autotest@autotest.ru'
    phone: str = '+7 (111) 111-11-11'
