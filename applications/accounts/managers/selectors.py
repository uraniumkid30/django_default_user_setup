from django.db.models.query import QuerySet

from core.repositories.base import BaseSelector
from applications.accounts.models import User
from .filters import UserFilter


class UserSelector(BaseSelector):
    @classmethod
    def get_queryset_filter(cls):
        return UserFilter

    @classmethod
    def get_model(cls):
        return User

    @classmethod
    def user_get_login_data(cls, *, user: User):
        return {
            "id": user.id,
            "username": user.username,
            "is_active": user.is_active,
            "is_admin": user.is_admin,
            "is_superuser": user.is_superuser,
        }

    @classmethod
    def list_users(cls, *, filters: dict = {}) -> QuerySet[User]:
        cls.fetch_records(**filters)
