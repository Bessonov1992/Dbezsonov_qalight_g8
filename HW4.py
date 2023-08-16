def first_task():  # first
    convert_data = input()
    convert_data = int(convert_data)
    print(convert_data)


try:
    first_task()
except ValueError:
    print("Entered not valid data")


def second_task():  # second
    first_data, second_data = input(), input()
    try:
        first_data, second_data = int(first_data), int(second_data)
        print(first_data + second_data)
    except ValueError:
        print(first_data + second_data)


second_task()


def third_task():  # third
    while True:
        data = input("input value\n")
        try:
            data = int(data)
            print("Thanks God!")
            break
        except ValueError:
            print("please type integer value")
            continue


third_task()


class OnlyEvenError(ArithmeticError):  # fourth
    def __init__(self, value):
        self.value = value


def check_digit(value):
    if value % 2 == 0:
        return value
    else:
        raise OnlyEvenError(f"не парне значення {value}")


print(check_digit(1))


def fivth_task(value):  # fiveth
    try:
        check_digit(value)
    except OnlyEvenError:
        value += 1
        print(value)
    else:
        value *= 2
        print(value)
    finally:
        print("Я все одно завжди щось друкую")


fivth_task(2)
