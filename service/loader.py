import json
from abc import ABC, abstractmethod
from typing import List, Dict


class DataLoader(ABC):
    @abstractmethod
    def load(self, path: str) -> List[Dict]:
        pass


class JsonDataLoader(DataLoader):
    def load(self, path: str) -> List[Dict]:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
