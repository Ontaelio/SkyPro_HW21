from classes.base import Storage

from exceptions import ItemNotFound, QtyNotEnough, NotEnoughSpace, ItemsLimitExceeded


class Shop(Storage):

    _max_unique_items = 5

    def __init__(self, items, capacity=20):
        if len(items) > self._max_unique_items:
            raise ItemsLimitExceeded
        super().__init__(items, capacity)

    def __str__(self):
        s = '\n'.join([line for line in self.get_items()])
        return (f"В магазине вместимостью {self.capacity} находятся:\n{s}\nСвободно: {self.get_free_space()} мест "
                f"на полках, {self._items_space()} товарных позиций.")

    @property
    def name(self):
        return 'магазин'

    def _items_space(self):
        return self._max_unique_items - len(self.items)

    def add(self, name, qty):
        if self.get_free_space() < qty:
            raise NotEnoughSpace
        if name in self.items:
            self.items[name] += qty
        else:
            if len(self.items) < self._max_unique_items:
                self.items[name] = qty
            else:
                raise ItemsLimitExceeded
        return True


# Some testing below

if __name__ == '__main__':
    try:
        a = Shop({'test': 23, 'bah': 34})
    except NotEnoughSpace as e:
        print(e.message)

    a = Shop({'test': 1, 'joy': 4})
    print(a)
    a.add('ugu', 4)
    print(a)
    try:
        a.add('aga', 30)
    except Exception as e:
        print(e.message)
    print(a)
    a.remove('ugu', 3)
    print(a)
    a.add('aga', 3)
    a.add('hhhaha', 1)
    print(a)
    print(a.get_unique_items_count())
    if 'aga' in a.items:
        print('Есть такой!')
    else:
        print('Нет такого!')
    a.remove('aga', 3)
    print(a.get_unique_items_count())
    try:
        a.remove('bah', 20)
    except QtyNotEnough as e:
        print(e.message)
    except ItemNotFound as e:
        print(e.message)

    a.add('s', 1)
    try:
        a.add('sss', 1)
    except Exception as e:
        print(e.message)

    a.remove('s', 1)
    try:
        a.add('sss', 1)
    except Exception as e:
        print(e.message)

    print(a)



