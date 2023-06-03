import datetime
from django.core.exceptions import ValidationError


class UserValidator:
    @staticmethod
    def validate_bithday(birthday: datetime.date):
        if birthday >= datetime.date.today():
            raise ValidationError("Birthday must be in the past")

    @staticmethod
    def validate_not_zero(value: int):
        if value == 0:
            raise ValidationError("Cannot be zero")
