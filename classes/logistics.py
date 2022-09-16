from __future__ import annotations

from classes.base import Storage
from classes.shop import Shop
from classes.store import Warehouse


class LogisticsAction:

    def __init__(self, source: Storage|None, destination: Storage|None, item, qty):
        self._source = source
        self._destination = destination
        self.item = item
        self.qty = qty

    def __repr__(self):
        return [self.source, self.destination, self.item, self.qty]

    def __str__(self):
        return f"Переместить {self.qty} {self.item} из {self.source.name} в {self.destination.name}."

    class _Placeholder:
        def __init__(self, name):
            self.name = name

    @property
    def source(self):
        if self._source:
            return self._source
        return self._Placeholder('завод')

    @property
    def destination(self):
        if self._destination:
            return self._destination
        return self._Placeholder('утиль')

    def _start(self):
        if self._source:
            try:
                self.source.remove(self.item, self.qty)
            except Exception as e:
                print(e.message)
                return False
            print(f"Нужное количество есть в {self.source.name}.")
        print(f"Курьер забрал {self.qty} {self.item} из {self.source.name}.")
        return True

    def _move(self, source, destination):
        print(f"Курьер везет {self.qty} {self.item} из {source.name} в {destination.name}.")
        return True

    def _finish(self):
        if self._destination:
            try:
                self.destination.add(self.item, self.qty)
            except Exception as e:
                print(e.message)
                self._rollback()
                return False
            print(f"Курьер доставил {self.qty} {self.item} в {self.destination.name}.")
        else:
            print(f"{self.qty} {self.item} отправлено в утиль.")
        return True

    def _rollback(self):
        if self._source:
            try:
                self.source.add(self.item, self.qty)
            except Exception as e:
                print('Случилась темпоральная дисфункция и все, вообще все поломалось!!!111')
                return False
        self._move(self.destination, self.source)
        print(f"{self.qty} {self.item} возвращено в {self.source.name}.")

    def execute(self):
        if self._start():
            if self._move(self.source, self.destination):
                if self._finish():
                    return True
        return False


# here be tests

if __name__ == '__main__':
    w = Warehouse({'печеньки': 32})
    s = Shop({})
    print(w)
    print(s)
    a = LogisticsAction(w, s, 'печеньки', 3)
    print(a)
    b = LogisticsAction(None, w, 'сегрегаторы', 23)
    print(b)
    c = LogisticsAction(s, None, 'утюги', 12)
    print(c)
    a.execute()
    b.execute()
    c.execute()
    print(w)
    print(s)
    d = LogisticsAction(s, None, 'печеньки', 2)
    d.execute()
    print(s)
    e = LogisticsAction(w, s, 'сегрегаторы', 20)
    e.execute()
