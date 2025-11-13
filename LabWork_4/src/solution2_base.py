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

A_range = range(0, A + 1)  # Створимо діапазон чисел (0; A]

def is_contain_same_digits(number: int) ->  bool:
    num_digits_map = Counter(str(number))  # підрахуємо кількість цифер в числі
    key, value = list(num_digits_map.items())[-1]  # візьмемо найбільшу пару значень цифри та її кількості
    if int(key) >= 5 and value == 2:  # перевіримо чи задовільняє умову число
        return True
    return False


for i in A_range:  # створимо цикл для перебору чисел діапазону
    if is_contain_same_digits(i):  # передаємо число до ф-ції
        first_number = i  # записуємо число у випадку успіху
        break  # виходимо з циклу у випадку успіху

for i in reversed(A_range):  # створимо цикл для перебору чисел діапазону з кінця
    if is_contain_same_digits(i):
        last_number = i
        break

print(f"Перше число в діапазоні (0; {A}] з двома однаковими цифрами {first_number}, а останнє {last_number}")
