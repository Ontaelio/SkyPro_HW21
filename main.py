from classes.base import Storage
from classes.request import Request
from classes.shop import Shop
from classes.store import Warehouse


def print_storages():
    s_list = {'warehouses': [], 'shops': []}

    for name, storage in Storage.all_places().items():
        if isinstance(storage, Warehouse):
            s_list['warehouses'].append(storage)
        if isinstance(storage, Shop):
            s_list['shops'].append(storage)

    print('\033[95mСклады:\033[39m')
    for wh in s_list['warehouses']:
        print(f"Склад \033[92m{wh.name}\033[39m вместимостью \033[97m{wh.capacity}\033[39m имеет "
              f"\033[93m{wh.get_free_space()}\033[39m свободных мест.")

    print('\033[95mМагазины:\033[39m')
    for shop in s_list['shops']:
        print(f"Магазин \033[92m{shop.name}\033[39m вместимостью \033[97m{shop.capacity}\033[39m имеет "
              f"\033[93m{shop.get_free_space()}\033[39m свободных мест "
              f"и \033[93m{shop.free_positions}\033[39m свободных товарных позиций.")
    print()


def main():
    command = input('Введите команду: ')

    if command.lower() in ['', 'список', 'проверить', 'чотам']:
        print_storages()
        return 1

    if command in Storage.all_places():
        print(Storage.all_places()[command], '\n')
        return 1

    if command.lower() not in ['выход', 'выйти', 'хватит']:
        request = Request(command)
        if request.action:
            action = request.create_action()
            if action.execute():
                print()
            else:
                print('Что-то пошло не так, действие не выполнено.')
                print()
        return 1

    return 0


if __name__ == '__main__':

    first_mighty_warehouse = Warehouse({'яиц': 20, 'питонов': 15}, capacity=200)
    second_mighty_warehouse = Warehouse({}, name='склад2', danger=3)
    warehouse_in_zhulebino = Warehouse({'золото': 1000}, name='жулебино', capacity=1000, danger=10)
    shop_on_main_street = Shop({}, capacity=50, positions=20, name='супермаг', danger=3)
    just_a_shop = Shop({})
    giant_shop_in_birulevo = Shop({}, name='бирюлево', capacity=500, positions=100, danger=10)

    print_storages()

    while main():
        ...



