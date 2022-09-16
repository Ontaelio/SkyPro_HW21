from classes.base import Storage

from exceptions import ItemNotFound, QtyNotEnough, NotEnoughSpace


class Store(Storage):

    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)

    def __str__(self):
        s = '\n'.join([line for line in self.get_items()])
        return f"Склад вместимостью {self.capacity} содержит:\n{s}\nСвободно: {self.get_free_space()} мест."

    @property
    def name(self):
        return 'склад'

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


