# Допишите в вашу задачу Archive обработку исключений.
# Добавьте исключение в ваш код InvalidTextError,
# которые будет вызываться, когда текст не является строкой или является пустой строкой.
#
# Текст ошибки: Invalid text: {введенный текст}. Text should be a non-empty string.'
#
# И InvalidNumberError, которое будет вызываться,
# если число не является положительным целым числом или числом с плавающей запятой.
#
# Текст ошибки: 'Invalid number: {введенное число}. Number should be a positive integer or float.'

from typing import Union


class MyException(Exception):
    pass


class InvalidTextError(MyException):
    pass


class InvalidNumberError(MyException):
    pass


class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: Union[int, float]):
        self.text = text
        self.number = number

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, value):
        if not isinstance(value, str) or value == '':
            raise InvalidTextError(f"Invalid text: {value}. Text should be a non-empty string.")
        self.__text = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise InvalidNumberError(f"Invalid number: {value}. Number should be a positive integer or float.")
        self.__number = value

    def __str__(self):
        return f'Text is {self.__text} and number is {self.__number}. ' \
               f'Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.__text}", {self.__number})'


if __name__ == '__main__':
    archive_instance = Archive("Sample text", 42.5)
    print(archive_instance)