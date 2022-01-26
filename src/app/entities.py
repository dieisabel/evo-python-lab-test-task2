__all__ = ['UserData']

from dataclasses import dataclass


@dataclass(frozen=True)
class UserData:
    first_name: str
    last_name: str

    def __hash__(self) -> int:
        return hash((self.first_name, self.last_name))
