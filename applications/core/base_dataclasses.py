from dataclasses import asdict


class DefaultSchema:
    def to_dict(self):
        return {k: v for k, v in asdict(self).items()}

    def choices(self):
        return [k for k, v in asdict(self).items()]

    def in_choices(self, value) -> bool:
        return value in self.choices()