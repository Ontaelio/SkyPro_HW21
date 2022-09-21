import json

from classes.base import Storage
from classes.logistics import LogisticsAction


class Request:
    """
    This class was required by the task, but here it actually handles parsing of the request string,
    and then creates a LogisticsAction object to carry out the task.
    """

    _possible_actions = ['доставить', 'утилизировать', 'создать']

    def __init__(self, order: str):
        parsed = order.split(' ')
        if len(parsed) > 4:
            self._parse_request(parsed)

        else:
            print('Неверный запрос.')
            self.action, self.amount, self.product, self.source, self.destination = None, None, None, None, None

    def __repr__(self):
        return json.dumps([self.action, self.product, self.amount, self.source, self.destination], ensure_ascii=False)

    def __str__(self):
        return str(self.__repr__())

    def _parse_request(self, parsed):

        # запрашиваемое действие
        self.action = parsed[0].lower()
        if self.action not in Request._possible_actions:
            print('Команда не опознана.')
            self.action = None
            return

        # количество
        try:
            self.amount = int(parsed[1])
        except ValueError:
            print('Количество задано неверно (буквы вместо цифр?).')
            self.action = None
            return
        if self.amount == 0:
            print('Ничего не происходит, потому что количество нулевое.')
            self.action = None
            return

        # товар
        self.product = parsed[2]

        # первый адрес
        self._source_name = parsed[4]
        if self._source_name not in Storage.all_places():
            if self.action == 'создать':
                print('Не понимаю, где создавать')
            else:
                print('Не понимаю, откуда забирать.')
            self.action = None
            return
        else:
            self.source = self._get_place_by_name(self._source_name)

        # второй адрес, если он подразумевается действием
        if self.action == 'доставить':
            try:
                self._destination_name = parsed[6]
                if self._destination_name not in Storage.all_places():
                    print('Не понимаю, куда доставлять.')
                    self.action = None
                    return
                else:
                    self.destination = self._get_place_by_name(self._destination_name)
            except IndexError as e:
                print('В команде не хватает слов (не указан адрес отправки/доставки?).')
                self.action = None
                return
        else:
            self.destination = None

    def _get_place_by_name(self, name):
        return Storage.all_places()[name]

    def create_action(self):

        if self.action == 'доставить':
            return LogisticsAction(self.source, self.destination, self.product, self.amount)

        if self.action == 'создать':
            return LogisticsAction(None, self.source, self.product, self.amount)

        if self.action == 'утилизировать':
            return LogisticsAction(self.source, None, self.product, self.amount)



# some tests here

if __name__ == '__main__':

    a = Request('Доставить 3 печеньки из склад в магазин')
    print(a)
    b = Request('Доставить 4 ёлки из магазин')
    с = Request('Убрать в столовой за 3 котами')
    d = Request('Доставить')
    print(d)
