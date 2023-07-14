from conf.core.base_dataclasses import BaseSchema
from dataclasses import dataclass


@dataclass
class EngineNames:
    sqlite: str = 'sqlite'
    postgres: str = 'postgres'


@dataclass
class BaseEngineSchema(BaseSchema):
    ENGINE: str
    NAME: str


@dataclass
class SqliteSchema(BaseEngineSchema):
    ENGINE: str = "django.db.backends.sqlite3"
    NAME: str


@dataclass
class PostgresqlSchema(BaseEngineSchema):
    ENGINE: str = "django.db.backends.sqlite3"
    NAME: str
    USER: str
    PASSWORD: str
    HOST: str = "127.0.0.1"
    PORT: str = "5432"
