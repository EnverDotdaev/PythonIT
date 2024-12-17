import doctest
from typing import Union

# TODO Написать 3 класса с документацией и аннотацией типов
class BankAccount:
    def __init__(self, account_number: int, balance: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер счета
        :param balance: Баланс на счете

        Примеры:
        >>> bank_account = BankAccount(1343246, 30700)  # инициализация экземпляра класса
        """
        if not isinstance(account_number, int):
            raise TypeError("Номер счета должен быть типа int")
        if account_number <= 0:
            raise ValueError("Номер счета должен быть положительным числом")
        self.account_number = account_number

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс на счете должно быть int или float")
        if balance < 0:
            raise ValueError("Баланс на счете не может быть отрицательным числом")
        self.balance = balance

    def is_on_balance(self) -> float:
        """
        Функция которая проверяет сколько средств на счету

        :return: Количество средств

        Примеры:
        >>> bank_account = BankAccount(1343246, 30700)
        >>> bank_account.is_on_balance()
        """

    def deposit(self, money: Union[int, float]) -> None:
        """
        Добавление средств на счет.
        :param money: Количество добавленных средств

        Примеры:
        >>> bank_account = BankAccount(1343246, 30700)
        >>> bank_account.deposit(3200)
        """
        if not isinstance(money, (int, float)):
            raise TypeError("Добавляемые средства должна быть типа int или float")
        if money < 0:
            raise ValueError("Добавляемые средства должна положительным числом")

    def withdrawal(self, money: Union[int, float]) -> None:
        """
        Снятие средств со счета.

        :param money: Количество снятых средств
        :raise ValueError: Если количество снимаемых средств превышает количество средств на счете,
        то возвращается ошибка.

        Примеры:
        >>> bank_account = BankAccount(1343246, 30700)
        >>> bank_account.withdrawal(7200)
        """

class Stock:
    def __init__(self, stock_quantity: int, stock_cost: Union[int, float]):
        """
                Создание и подготовка к работе объекта "Акции"

                :param stock_quantity: Количество акций
                :param stock_cost: Стоимость акции

                Примеры:
                >>> stock = Stock(200, 30)  # инициализация экземпляра класса
                """
        if not isinstance(stock_quantity, int):
            raise TypeError("Количество акций должно быть типа int")
        if stock_quantity <= 0:
            raise ValueError("Количество акций должно быть положительным числом")
        self.stock_quantity = stock_quantity

        if not isinstance(stock_cost, (int, float)):
            raise TypeError("Стоимость акции должна быть int или float")
        if stock_cost <= 0:
            raise ValueError("Стоимость акции должна быть больше нуля")
        self.stock_cost = stock_cost

    def add_stock(self,quantity: int) -> None:
        """
                Добавление акций.

                :param quantity: Количество добавляемых акций

                Примеры:
                >>> stock = Stock(200, 30)
                >>> stock.add_stock(50)
                """
        if not isinstance(quantity, int):
            raise TypeError("Количество добавляемых акций должно быть типа int")
        if quantity < 0:
            raise ValueError("Количество добавляемых акций должно быть положительным числом")

    def remove_stock(self,quantity: int) -> None:
        """
                Добавление акций.

                :param quantity: Количество убираемых акций
                :raise ValueError: Если количество убираемых акций превышает количество акций,
                то возвращается ошибка.

                Примеры:
                >>> stock = Stock(200, 30)
                >>> stock.remove_stock(50)
                """
        if not isinstance(quantity, int):
            raise TypeError("Количество убираемых акций должно быть типа int")
        if quantity < 0:
            raise ValueError("Количество убираемых акций должно быть положительным числом")

    def change_cost(self, value: Union[int, float]) -> None:
        """
                Изменение цены акций.

                :param value: Изменение цены
                :raise ValueError: Если удешевление акции превышает цену акции,
                то возвращается ошибка.

                Примеры:
                >>> stock = Stock(200, 30)
                >>> stock.change_cost(10)
                """
        if not isinstance(value, (int, float)):
            raise TypeError("Количество убираемых акций должно быть типа int или float")

class Youtube:
    def __init__(self, subscribers: int, views: int):
        """
                Создание и подготовка к работе объекта "Youtube"

                :param subscribers: Количество подписчиков
                :param views: Количество просмотров

                Примеры:
                >>> youtube = Youtube(20000, 600000)  # инициализация экземпляра класса
                """
        if not isinstance(subscribers, int):
            raise TypeError("Количество подписчиков должно быть типа int")
        if subscribers < 0:
            raise ValueError("Количество подписчиков не может быть отрицательным")
        self.subscribers = subscribers

        if not isinstance(views ,int):
            raise TypeError("Количество просмотров должно быть int")
        if views <= 0:
            raise ValueError("Количество просмотров должно быть больше нуля")
        self.stock_cost = views

    def add_sub(self,sub: int) -> None:
        """
                Увеличение числа подписчиков

                :param sub: Количество новых подписчиков

                Примеры:
                >>> youtube = Youtube(20000, 600000)
                >>> youtube.add_sub(5000)
                """
        if not isinstance(sub, int):
            raise TypeError("Добавляемые подписчики должны быть типа int")
        if sub < 0:
            raise ValueError("Добавляемые подписчики должны положительным числом")

    def remove_sub(self,sub: int) -> None:
        """
                Уменьшение числа подписчиков

                :param sub: Количество убраных подписчиков
                :raise ValueError: Если количество убраных подписчиков превышает количество подпистиков,
                то возвращается ошибка.

                Примеры:
                >>> youtube = Youtube(20000, 600000)
                >>> youtube.remove_sub(1000)
                """
        if not isinstance(sub, int):
            raise TypeError("Количество убранных подписчиков должно быть типа int")
        if sub < 0:
            raise ValueError("Количество убранных подписчиков должно быть положительным числом")

    def have_sub(self) -> bool:
        """
                Функция которая проверяет есть ли подписчики

                :return: Есть ли подписчики

                Примеры:
                >>> youtube = Youtube(20000, 600000)
                >>> youtube.have_sub()
                """

if __name__ == "main":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass


