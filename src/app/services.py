__all__ = ['IUserDataService', 'UserDataService']

from abc import ABC
from abc import abstractmethod
from typing import List

from entities import UserData
from repositories import IUserDataRepository
from repositories import UserDataRepository


class IUserDataService(ABC):
    @abstractmethod
    def add(self, data: UserData) -> bool:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> List[UserData]:
        raise NotImplementedError


class UserDataService(IUserDataService):
    def __init__(self):
        self._repository: IUserDataRepository = UserDataRepository()

    def add(self, data: UserData) -> bool:
        if self._repository.check_in(data):
            return False
        self._repository.add(data)
        return True

    def find_all(self) -> List[UserData]:
        return self._repository.find_all()
