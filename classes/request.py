
class Request:

    def __init__(self, order: str):
        parsed = order.split(' ')
        self.action = parsed[0]
        self.amount = parsed[1]
        self.product = parsed[2]
        self.source = parsed[4]
        self.destination = parsed[6]

    def __repr__(self):
        return [self.action, self.product, self.amount, self.source, self.destination]

    def __str__(self):
        return str(self.__repr__())


# some tests here

if __name__ == '__main__':

    a = Request('Доставить 3 печеньки из склад в магазин')
    print(a)
