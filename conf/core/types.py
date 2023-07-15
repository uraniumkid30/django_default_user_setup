from typing import TypeVar
from decimal import Decimal

from django.db import models


# Generic type for a Django model
DjangoModelType = TypeVar("DjangoModelType", bound=models.Model)
Money = TypeVar("Money", bound=Decimal)
Number = TypeVar("Number", int, float, Decimal)