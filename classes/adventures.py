import random

from classes.shop import Shop
from classes.store import Warehouse


class Adventure:
    """
    An additional static class to make life fun for the courier. Basically, it serves as a placeholder
    for real-life possible scenarios en-route.
    """

    @staticmethod
    def hopniks(package):
        loss = random.randrange(package.qty - 1) + 1
        print(f'\033[91mО нет! На курьера напали гопники и украли \033[97m{loss}\033[91m {package.item}!\033[39m')
        package.qty -= loss
        return package

    @staticmethod
    def evil_martians(package):
        martian_items = ['будьбузавры', 'улетатели-222', 'штожэтотакоехосподижмой', 'яйца_шиповыдувальщика']
        if package.destination.name not in ['утиль']:
            if len(package.destination.items) > 3:
                new_item = random.choice(list(package.destination.items))
            else:
                new_item = random.choice(martian_items)
            print(f'\033[91mВнезапные марсиане похитили курьера и превратили \033[97m{package.item}\033[91m в'
                  f' \033[95m{new_item}\033[91m!\033[39m')
            package.item = new_item
            return package
        return None

    @staticmethod
    def oh_no(package):
        print(f'\033[91mКурьер уехал куда-то не туда и пропал. Товар потерян.\033[39m')
        package.qty = 0
        return package

    @staticmethod
    def change_of_heart(package):
        if package.source.name not in ['завод']:
            print(f'\033[91mКурьер передумал и вернулся в \033[97m{package.source.name}\033[91m.\033[39m')
            package.destination = package.source
            return package
        return None

    @staticmethod
    def happens(package):
        dng = 21 - (package.destination.danger + package.source.danger)
        if dng != 21:
            if not random.randrange(dng):
                choice = random.randrange(4)
                if choice == 0:
                    return Adventure.hopniks(package)
                if choice == 1:
                    return Adventure.evil_martians(package)
                if choice == 2:
                    return Adventure.change_of_heart(package)
                return Adventure.oh_no(package)
        return None


# Some testing below
#
# if __name__ == '__main__':
#     w = Warehouse({'печеньки': 32, 'кубышки': 2, 'лопаты': 3, 'арбузы': 1, 'ёжики': 5, 'белки': 1}, danger=7)
#     s = Shop({'кубышки': 2, 'лопаты': 3}, danger=10)
#     print(w)
#     print(s)
#     a = LogisticsAction(w, s, 'печеньки', 3)
#     a = Adventure.happens(a)
#     print(a)
