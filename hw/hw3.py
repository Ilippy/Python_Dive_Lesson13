# В организации есть два типа людей: сотрудники и обычные люди.
# Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
#
# Фамилия (строка, не пустая)
# Имя (строка, не пустая)
# Отчество (строка, не пустая)
# Возраст (целое положительное число)
#
# Сотрудники имеют также уникальный идентификационный номер (ID),
# который должен быть шестизначным положительным целым числом.
#
# Ваша задача:
#
# Создать класс Person,
# который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
# Класс должен проверять валидность входных данных
# и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
#
# Создать класс Employee,
# который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
#
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
#
# Добавить метод get_level в класс Employee,
# который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
#
# Создать несколько объектов класса Person и Employee с разными данными и проверить,
# что исключения работают корректно при передаче неверных данных.

class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        # print(f"{value = }, {isinstance(self.name, str) = }, {len(value.strip()) = }")
        if not isinstance(self.name, str) or len(value.strip()) == 0:
            raise InvalidNameError(f"Invalid name: {value}. Name should be a non-empty string.")
        setattr(instance, self.name, value)


class Person:
    last_name = NameDescriptor()
    first_name = NameDescriptor()
    patronymic = NameDescriptor()

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age <= 0:
            raise InvalidAgeError(f"Invalid age: {age}. Age should be a positive integer.")
        self.__age = age

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def __str__(self):
        return f"{self._last_name} {self._first_name} {self._patronymic} {self.__age}"


class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, id_: int):
        super().__init__(last_name, first_name, patronymic, age)
        self.id = id_

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) or len(str(value)) != 6 or value <= 0:
            raise InvalidIdError(
                f"Invalid id: {value}. Id should be a 6-digit positive integer between 100000 and 999999.")
        self.__id = value

    def get_level(self):
        return sum(map(int, str(self.id))) % 7


if __name__ == '__main__':
    try:
        t1 = Person("", "John", "Doe", 30)
    except InvalidNameError as e:
        assert str(e) == "Invalid name: . Name should be a non-empty string."

    try:
        t2 = Person("Alice", "Smith", "Johnson", -5)
    except InvalidAgeError as e:
        assert str(e) == "Invalid age: -5. Age should be a positive integer."

    try:
        t3 = Employee("Bob", "Johnson", "Brown", 40, 12345)
    except InvalidIdError as e:
        assert str(e) == "Invalid id: 12345. Id should be a 6-digit positive integer between 100000 and 999999."

    t4 = Person("Alice", "Smith", "Johnson", 25)
    assert t4.get_age() == 25

    print("Все тесты прошли успешно!")
