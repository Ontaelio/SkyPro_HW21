from classes.base import Storage

from exceptions import ItemNotFound, QtyNotEnough, NotEnoughSpace, ItemsLimitExceeded


class Shop(Storage):
    """
    A class for Shop objects
    """

    _max_unique_items = 5

    def __init__(self, items, capacity=20, positions=_max_unique_items, name='магазин', danger=0):
        self.positions = positions
        if len(items) > self.positions:
            raise ItemsLimitExceeded
        super().__init__(items, capacity, name, danger)

    def __str__(self):
        goods_list = [line for line in self.get_items()]

        if not goods_list:
            return f"Магазин \033[92m{self.name}\033[39m вместимостью \033[97m{self.capacity}\033[39m пуст."

        s = '\n'.join(goods_list)
        return (f"В магазине \033[92m{self.name}\033[39m вместимостью \033[97m{self.capacity}\033[39m находятся:\n\033[36m{s}\033[39m\n"
                f"Свободно: \033[93m{self.get_free_space()}\033[39m мест "
                f"на полках, \033[93m{self._items_space()}\033[39m товарных позиций.")

    @property
    def name(self):
        return self._name

    @property
    def free_positions(self):
        return self._items_space()

    def _items_space(self):
        return self.positions - len(self.items)

    def add(self, name, qty):
        if self.get_free_space() < qty:
            raise NotEnoughSpace
        if name in self.items:
            self.items[name] += qty
        else:
            if len(self.items) < self.positions:
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



