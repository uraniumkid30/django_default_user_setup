import re
from typing import NoReturn


class UserValidation:
    @staticmethod
    def email_is_valid(value: str) -> NoReturn:
        pattern: str = "/^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/"
        if not re.match(pattern, value):
            raise ValueError(f"Invalid email {value}")

    @staticmethod
    def phone_number_is_valid(value: str) -> NoReturn:
        pattern: str = '\+?[0-9]{10,18}'
        if not re.match(pattern, value):
            raise ValueError(f"Invalid phone number {value}")

    @staticmethod
    def phone_number_is_valid_nig(value: str) -> NoReturn:
        pattern: str = '\A(?=(\+?234[^0]+)).{10,16}'
        if not re.match(pattern, value):
            raise ValueError(f"Invalid phone number {value}")

    @staticmethod
    def superuser_is_valid(value: bool) -> NoReturn:
        if value is not True:
            raise ValueError('Superuser must have is_superuser=True.')
