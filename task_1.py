import random


if __name__ == "__main__":

    class Character:
        """ Базовый класс персонаж. """

        def __init__(self, health: int, strength: int, speed: int):
            """
                    Создание и подготовка к работе объекта "Персонаж"

                    :param health: Количество очков здоровья
                    :param strength: Значение силы
                    :param speed: Значение скорости

                    Примеры:
                    >>> character = Character(200, 30, 15) # инициализация экземпляра класса
                    """
            self._max_health = health
            self.health = health
            self._strength = strength
            self._speed = speed

        @property
        def max_health(self) -> int:
            """Возвращает максимум очков здоровья."""
            return self._max_health

        @property
        def health(self) -> int:
            """Возвращает очки здоровья."""
            return self._health

        @health.setter
        def health(self, current_health: int) -> None:
            """Устанавливает очки здоровья."""
            if not isinstance(current_health, int):
                raise TypeError("Очки здоровья должны быть типа int")
            if current_health <= 0:
                raise ValueError("Очки здоровья должны быть положительным числом")
            self._health = current_health

        @property
        def strength(self) -> int:
            """Возвращает очки выносливости."""
            return self._strength

        @property
        def speed(self) -> int:
            """Возвращает скорость."""
            return self._speed

        def heal(self, heal_value: int = 50) -> int:
            """
                    Лечение персонажа.

                    :param heal_value: Значение лечения

                    Примеры:
                    >>> character = Character(200, 30, 15)
                    >>> character.heal()
                    """
            if not isinstance(heal_value, int):
                raise TypeError("Лечение должно быть типа int")
            if heal_value <= 0:
                raise ValueError("Лечение должно быть положительным числом")
            if self.health == self.max_health:
                print(f"Лечение не требуется.")
                return self.health
            elif (self.max_health - self.health) < heal_value:
                print(f'Здоровье восстановлено на {self.max_health - self.health}.')
                self.health += self.max_health - self.health
                return self.health
            else:
                self.health += heal_value
                print(f'Здоровье восстановлено на {heal_value}.')
                return self.health

        def get_damage(self, damage: int = 50) -> int:
            """
                    Получение урона.

                    :param damage: Значение получаемого урона

                    Примеры:
                    >>> character = Character(200, 30, 15)
                    >>> character.get_damage()
                    """
            if not isinstance(damage, int):
                raise TypeError("Урон должен быть типа int")
            if damage <= 0:
                raise ValueError("Урон должен быть положительным числом")
            if random.randint(1, 100) < self.speed:
                print(f"Вы увернулись. {str()}")
                return self.health
            self.health -= damage
            print(f"Вы получили {damage} урона.")
            return self.health

        def deal_damage(self, damage: int = 50) -> int:
            """
                    Нанесение урона.

                    :param damage: Значение нанесенного урона

                    Примеры:
                    >>> character = Character(200, 30, 15)
                    >>> character.deal_damage()
                    """
            if not isinstance(damage, int):
                raise TypeError("Урон должен быть типа int")
            if damage <= 0:
                raise ValueError("Урон должен быть положительным числом")
            damage += self._strength
            print(f"Нанесено {damage} урона")
            return damage

        def __str__(self) -> str:
            return f"Здоровье персонажа класса {self.__class__.__name__}: {self.health!r}/{self.max_health!r}."

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(health={self.health!r}, strength={self.strength!r}, speed={self.speed!r})"


    class Warrior(Character):
        """Дочерний класс персонаж воин."""

        def __init__(self, health: int, strength: int, speed: int, armor: int):
            """
                    Создание и подготовка к работе объекта "Воин"

                    :param health: Количество очков здоровья
                    :param strength: Значение силы
                    :param speed: Значение скорости
                    :param armor: Значение брони

                    Примеры:
                    >>> warrior = Warrior(200, 30, 15, 20) # инициализация экземпляра класса
                    """
            super().__init__(health, strength, speed) # наследование __init__ из базового класса
            self._armor = armor

        @property
        def armor(self) -> int:
            """Возвращает значение брони."""
            return self._armor

        def get_damage(self, damage: int = 50) -> int:
            """
                    Получение урона.(С учетом брони)

                    :param damage: Значение получаемого урона

                    Примеры:
                    >>> warrior = Warrior(200, 30, 15, 20)
                    >>> warrior.get_damage()
                    """
            if not isinstance(damage, int):
                raise TypeError("Урон должен быть типа int")
            if damage <= 0:
                raise ValueError("Урон должен быть положительным числом")
            if random.randint(1, 100) < self.speed:
                print(f"Вы увернулись.")
                return self.health
            damage -= self.armor
            if damage <= 0:
                print(f"Броня защитила.")
                return self.health
            self.health -= damage
            print(f"Вы получили {damage} урона.")
            return self.health

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(health={self.health!r}, strength={self.strength!r}, speed={self.speed!r}, armor={self.armor})"


    class Archer(Character):
        """Дочерний класс персонаж лучник."""

        def __init__(self, health: int, strength: int, speed: int, accuracy: int):
            """
                    Создание и подготовка к работе объекта "Лучник"

                    :param health: Количество очков здоровья
                    :param strength: Значение силы
                    :param speed: Значение скорости
                    :param accuracy: Значение точности

                    Примеры:
                    >>> archer = Archer(200, 30, 15, 40) # инициализация экземпляра класса
                    """
            super().__init__(health, strength, speed) # наследование __init__ из базового класса
            self._accuracy = accuracy

        @property
        def accuracy(self) -> int:
            """Возвращает значение точности."""
            return self._accuracy

        def deal_damage(self, damage: int = 50) -> int:
            """
                    Нанесение урона.(С учетом точности)

                    :param damage: Значение нанесенного урона

                    Примеры:
                    >>> archer = Archer(200, 30, 15, 40)
                    >>> archer.deal_damage()
                    """
            if not isinstance(damage, int):
                raise TypeError("Урон должен быть типа int")
            if damage <= 0:
                raise ValueError("Урон должен быть положительным числом")
            if random.randint(1, 100) > self.accuracy:
                print("Промах")
                damage = 0
                return damage
            damage += self._strength
            print(f"Нанесено {damage} урона")
            return damage

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(health={self.health!r}, strength={self.strength!r}, speed={self.speed!r}, accuracy={self.accuracy})"

    pass

