__all__ = ['IUserDataRepository', 'UserDataRepository']

from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Dict

from entities import UserData


class IUserDataRepository(ABC):
    @abstractmethod
    def add(self, data: UserData) -> None:
        raise NotImplementedError

    @abstractmethod
    def check_in(self, data: UserData) -> bool:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[UserData]:
        raise NotImplementedError


class UserDataRepository(IUserDataRepository):
    def __init__(self):
        self._storage: Dict[UserData, None] = dict()

    def add(self, data: UserData) -> None:
        self._storage.update({data: None})

    def check_in(self, data: UserData) -> bool:
        if data in self._storage.keys():
            return True
        return False

    def find_all(self) -> List[UserData]:
        return list(self._storage.keys())
