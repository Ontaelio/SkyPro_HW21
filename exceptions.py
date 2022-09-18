class ItemNotFound(Exception):
    message = 'Такой товар не найден.'


class QtyNotEnough(Exception):
    message = 'Недостаточно единиц товара.'


class NotEnoughSpace(Exception):
    message = 'Недостаточно места.'


class ItemsLimitExceeded(Exception):
    message = 'Превышен лимит товарных позиций.'


class StorageNameAlreadyExists(Exception):
    message = 'Место с таким названием уже существует'
