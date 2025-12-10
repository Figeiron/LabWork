while True:
    try:
        number = input("Введіть тризначне число: ")

        if len(number) != 3:
            raise ValueError("Введено некоректне число")

        number = int(number)
        break

    except ValueError as error:
        print(error)


def find_palindrome(n: int) -> int:  # задамо ф-цію для пошуку паліндрому числа
    return int(str(n)[::-1])  # Перетворимо число в текст інвертуємо його після чого повернемо в число


def brut_force_equation(
        func):  # задамо ф-цію для перебору значень з заданим рівнянням котре задається безіменною ф-цією
    for x in range(1, 1000):  # переберемо всі можливі числа
        if func(x):  # перевіримо відповідність числа до рівняння
            return x


print("Початкове число сума якого з паліндромом дорівнює {}".format(number))
palindrome = brut_force_equation(  # виклечемо ф-цію
    lambda x: (x + find_palindrome(x)) == number  # задамо рівняння у форматі безіменної ф-ції
)

if palindrome:
    print(palindrome)
else:
    print("Не знайдено")
