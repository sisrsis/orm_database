from abc import ABC, abstractmethod


class BaseDatabase(ABC):
    def __init__(self, name: str, uri: str):
        self.config = {}
        self.config['name'] = name
        self.config['uri'] = uri

    @abstractmethod
    async def start(self):
        pass

    @abstractmethod
    async def insert_one(self, collection: str, value: dict):
        pass

    @abstractmethod
    async def insert_list(self, collection: str, value: list):
        pass

    @abstractmethod
    async def create(self, collection: str, field: dict):
        pass

    @abstractmethod
    async def find_one(self):
        pass