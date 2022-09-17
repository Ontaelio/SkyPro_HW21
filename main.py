from classes.request import Request
from classes.shop import Shop
from classes.store import Warehouse


def main(a, b):
    command = input('Введите команду: ')

    if command.lower() in ['', 'список', 'проверить', 'чотам']:
        print(wh)
        print(shop)
        print()
        return 1

    if command.lower() not in ['выход', 'выйти', 'хватит']:
        request = Request([a, b], command)
        if request.action:
            action = request.create_action()
            if action.execute():
                print(wh)
                print(shop)
                print()
            else:
                print('Что-то пошло не так, действие не выполнено.')
                print()
        return 1

    return 0


if __name__ == '__main__':

    wh = Warehouse({'яиц': 20, 'питонов': 15})
    shop = Shop({})
    print(wh)
    print(shop)
    print()

    while main(wh, shop):
        ...



