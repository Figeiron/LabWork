"""
Завдання взяті з лабораторної роботи номер 4
"""


# Переробка завдання 1
class BirthDate:
    def __init__(self, birthday_string: str):
        if len(birthday_string) != 8:
            raise ValueError

        self.birthday = birthday_string
        self.day = int(birthday_string[:2:])
        self.month = int(birthday_string[2:4:])
        self.year = int(birthday_string[4::])


def solution1(A, B, birthday: BirthDate):
    if A == birthday.day:
        print("A == дню народження")
    else:
        print("A не != дню народження")

    if B == birthday.day:
        print("B == дню народження")
    else:
        print("B не != дню народження")

    if A == birthday.month:
        print("A == місяцю народження")
    else:
        print("A не != місяцю народження")

    if B == birthday.month:
        print("B == місяцю народження")
    else:
        print("B не != місяцю народження")

    if A == birthday.year:
        print("A == року народження")
    else:
        print("A != року народження")

    if B == birthday.year:
        print("B == року народження")
    else:
        print("B != року народження")


while True:
    try:
        A = int(input("Введіть A: "))
        B = int(input("Введіть B: "))

        birthday = BirthDate(input("Введіть дату народження(ddmmyyyy):"))
        solution1(A, B, birthday)
        break

    except ValueError:
        print("Спробуйте знову")


# переробка завдання 2

def check_condition_2(variables: list):
    return len(variables) == 5


def solution2(variables: list):
    if check_condition_2(variables):
        count = 0

        for i in range(5):
            for j in range(5):
                if i != j and variables[j] != 0:
                    if variables[i] % variables[j] == 0:
                        count += 1
        return count


while True:
    try:
        variables = []

        for i in range(5):
            variables.append(int(input("Введіть значення для x{}: ".format(i + 1))))

        print(solution2(variables), "чисел, є дільниками інших чисел массиву")
        break

    except ValueError:
        print("Спробуйте знову")


# переробка завдання 3
def str_to_digit_list(num):
    return list(map(int, list(num)))


while True:
    try:
        A = input("Введіть A: ")
        B = input("Введіть B: ")

        a_base = max(str_to_digit_list(A)) + 1
        b_base = max(str_to_digit_list(B)) + 1

        print("Мінімально можлива числення для числа А:", a_base)
        print("Мінімально можлива числення для числа В:", b_base)

        print("Число А в десятковій системі:", int(A, a_base))
        print("Число В в десятковій системі:", int(B, b_base))
        break

    except ValueError:
        print("Спробуйте знову")
