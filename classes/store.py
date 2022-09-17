from classes.base import Storage

from exceptions import ItemNotFound, QtyNotEnough, NotEnoughSpace


class Store(Storage):

    def __init__(self, items, capacity=100, name='склад'):
        super().__init__(items, capacity, name)

    def __str__(self):
        goods_list = [line for line in self.get_items()]

        if not goods_list:
            return f"Склад вместимостью \033[97m{self.capacity}\033[39m пуст."

        s = '\n'.join(goods_list)
        return f"Склад вместимостью \033[97m{self.capacity}\033[39m содержит:\n\033[36m{s}\033[39m\nСвободно: " \
               f"\033[93m{self.get_free_space()}\033[39m мест."

    @property
    def name(self):
        return self._name

    def add(self, name, qty):
        if self.get_free_space() < qty:
            raise NotEnoughSpace
        if name in self.items:
            self.items[name] += qty
        else:
            self.items[name] = qty
        return True


class Warehouse(Store):
    """
    The right name for this class! Store == shop in English!
    """
    pass


# Some testing below

if __name__ == '__main__':
    a = Warehouse({'test': 23, 'bah': 34})
    print(a)
    a.add('ugu', 40)
    print(a)
    try:
        a.add('aga', 30)
    except Exception as e:
        print(e.message)
    print(a)
    a.remove('bah', 30)
    print(a)
    a.add('aga', 30)
    a.add('hhhaha', 1)
    print(a)
    print(a.get_unique_items_count())
    if 'aga' in a.items:
        print('Есть такой!')
    else:
        print('Нет такого!')
    a.remove('aga', 30)
    print(a.get_unique_items_count())
    try:
        a.remove('bah', 20)
    except QtyNotEnough as e:
        print(e.message)
    except ItemNotFound as e:
        print(e.message)

    print(repr(a))


