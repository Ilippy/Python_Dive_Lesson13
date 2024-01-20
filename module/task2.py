# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def task2(dictionary: dict, key, default_value):
    try:
        default_value = dictionary[key]
    except KeyError:
        # dictionary[key] = default_value
        pass
    return default_value


def main():
    d = {1: "one", 2: "two", 3: "three", 4: "four"}
    print(task2(d, 1, 1))
    print(task2(d, 5, 1))


if __name__ == '__main__':
    main()
