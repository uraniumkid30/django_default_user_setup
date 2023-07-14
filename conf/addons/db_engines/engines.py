from dataclasses import dataclass

from .base import BaseEngine
from .enums import SqliteSchema, PostgresqlSchema


class PostgresqlEngine(BaseEngine):
    @classmethod
    def get_schema(cls) -> dataclass:
        """ """
        return PostgresqlSchema


class SqliteEngine(BaseEngine):
    @classmethod
    def get_schema(cls) -> dataclass:
        """ """
        return SqliteSchema
