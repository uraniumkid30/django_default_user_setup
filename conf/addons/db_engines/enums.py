from conf.core.base_dataclasses import BaseSchema
from dataclasses import dataclass, field


@dataclass(frozen=True)
class EngineNames:
    sqlite: str = 'sqlite'
    postgres: str = 'postgres'


@dataclass(frozen=True)
class BaseEngineSchema(BaseSchema):
    ENGINE: str
    NAME: str


@dataclass(frozen=True)
class SqliteSchema(BaseEngineSchema):
    ENGINE: str = field(default="django.db.backends.sqlite3", init=False)


@dataclass(frozen=True)
class PostgresqlSchema(BaseEngineSchema):
    ENGINE: str = field(default="django.db.backends.sqlite3", init=False)
    USER: str
    PASSWORD: str
    HOST: str = field(default="127.0.0.1")
    PORT: str = field(default="5432")
