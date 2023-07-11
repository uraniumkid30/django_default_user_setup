from typing import List

from applications.accounts.models import User
from applications.core.repositories.base import BaseService


class UserService(BaseService):
    @classmethod
    def get_model(cls):
        return User

    @classmethod
    def get_updatable_fields(cls) -> List[str]:
        return None

    @classmethod
    def create_user(
        cls,
        *,
        data: dict = {},
    ) -> User:
        """Creates User"""
        user = cls.create_record(**data)

        return user

    @classmethod
    def update_user(cls, *, user: User, data: dict = {}) -> User:
        update_user, is_updated = cls.create_record(
            user, **data
        )
        return update_user or user
