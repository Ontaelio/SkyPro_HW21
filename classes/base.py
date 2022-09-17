import json
from abc import ABC, abstractmethod
from typing import Optional

from exceptions import ItemNotFound, QtyNotEnough, NotEnoughSpace


class Storage(ABC):

    def __init__(self, items: dict, capacity: int, name: Optional[str] = None):
        self._items = items
        self._capacity = capacity
        if self._space_used() > capacity:
            raise NotEnoughSpace
        self._name = name

    def __repr__(self):
        return json.dumps([self.capacity, self.items], ensure_ascii=False)

    @abstractmethod
    def __str__(self):
        pass

    @property
    def items(self):
        return self._items

    @property
    @abstractmethod
    def name(self):
        pass
    
    @property
    def capacity(self):
        return self._capacity

    @classmethod
    def all_places(cls):
        return Storage._all_names

    @abstractmethod
    def add(self, name, qty):
        pass

    def remove(self, name, qty):
        if name not in self.items:
            raise ItemNotFound
        if self.items[name] < qty:
            raise QtyNotEnough
        self.items[name] -= qty
        if self.items[name] == 0:
            del self.items[name]
        return True

    def _space_used(self):
        return sum(self.items[name] for name in self.items)

    def get_free_space(self):
        return self.capacity - self._space_used()

    def get_items(self):
        ls = []
        for item, qty in self.items.items():
            ls.append(': '.join([item, str(qty)]))
        return ls

    def get_unique_items_count(self):
        return len(self.items)
