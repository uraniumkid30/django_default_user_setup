from dataclasses import dataclass, asdict


class DefaultSchema:
    def to_dict(self):
        return {k: v for k, v in asdict(self).items()}

    def choices(self):
        return [k for k, v in asdict(self).items()]

    def in_choices(self, value) -> bool:
        return value in self.choices()


@dataclass(frozen=True)
class LibraryManagerConfigurationSchema(DefaultSchema):
    # List = field(default_factory=lambda: ["loyalty"])
    pipfile_path: str = "pipfile.lock"
    base_path: str = "requirements/base.txt"
    development_path: str = "requirements/development.txt"


@dataclass(frozen=True)
class LibraryManagers(DefaultSchema):
    PIP: str = "PIP"
    PIPENV: str = "PIPENV"
