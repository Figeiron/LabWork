from collections import Counter

while True:
    print("Введіть сотні десятки і десятки до числа A")
    try:
        a3 = int(input("Введіть сотні: ")[0])
        a2 = int(input("Введіть десятки: ")[0])
        a1 = int(input("Введіть одиниці: ")[0])
        break

    except ValueError:
        print("Спробуйте знову")

A = a3 * 100 + a2 * 10 + a1  # складаємо задані цифри в число A

first_number = None  # ініціалізуємо змінні для збереження чисел задовільняючих умову
last_number = None


def find_same_digits(number: int) -> None | int:
    num_digits_map = Counter(str(number))  # підрахуємо кількість цифер в числі
    key, value = list(num_digits_map.items())[-1]  # візьмемо найбільше пару значень цифри та її кількості
    if int(key) >= 5 and value == 2:  # перевіримо чи задовільняє умову число
        return number  # повертаєм значення в випадку успіху
    return None


for i in range(int(A) + 1):  # створюємо цикл для перебору значень в діапазоні (0; A]
    first_number = find_same_digits(i)  # передаємо результат ітерації в ф-цію в випадку успіху отримаємо це ж число
    if first_number:
        break  # виходимо з циклу у випадку успіху

for i in range(int(A), -1, -1):  # створюємо цикл для перебору значень в діапазоні [A; 0)
    last_number = find_same_digits(i)
    if last_number:
        break

print(f"Перше число в діапазоні [0; {A}] з двома однаковими цифрами {first_number}, а останнє {last_number}")
