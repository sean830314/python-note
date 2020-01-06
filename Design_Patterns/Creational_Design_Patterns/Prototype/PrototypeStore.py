from enum import Enum
from pts import pt, PrototypeFatbook, PrototypeGoople

class StoreEnum(Enum):
    Goople = 1,
    Fatbook = 2,
    Amozoo = 3


class PrototypeStore:

    _prototypes = {}

    def add(self, store=StoreEnum, prototype=pt):
        self._prototypes[store] = prototype

    def get(self, store=StoreEnum):
        return self._prototypes[store].clone()