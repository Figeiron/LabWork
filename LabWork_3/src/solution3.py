while True:
    try:
        A = input("Введіть A: ")
        B = input("Введіть B: ")

        if not A.isdigit() or not B.isdigit():
            raise ValueError
        break

    except ValueError:
        print("Спробуйте знову")

a_base = 0  # ініціалізуємо змінну для збереження сис.числення числа

if "1" in A:  # Перевіримо чи є деяка цифра в числі для отримання сис.числення
    a_base = 2  # Запишемо в змінну сис.числення для числа в разу успіху
if "2" in A:
    a_base = 3
if "3" in A:
    a_base = 4
if "4" in A:
    a_base = 5
if "5" in A:
    a_base = 6
if "6" in A:
    a_base = 7
if "7" in A:
    a_base = 8
if "8" in A:
    a_base = 9
if "9" in A:
    a_base = 10

b_base = 0  # ініціалізуємо змінну для збереження сис.числення числа

if "1" in B:  # Перевіримо чи є деяка цифра в числі для отримання сис.числення
    b_base = 2  # Запишемо в змінну сис.числення для числа в разу успіху
if "2" in B:
    b_base = 3
if "3" in B:
    b_base = 4
if "4" in B:
    b_base = 5
if "5" in B:
    b_base = 6
if "6" in B:
    b_base = 7
if "7" in B:
    b_base = 8
if "8" in B:
    b_base = 9
if "9" in B:
    b_base = 10

print("Мінімально можлива числення для числа А:", a_base)
print("Мінімально можлива числення для числа В:", b_base)

print("Число А в десятковій системі:", int(A, a_base))
print("Число В в десятковій системі:", int(B, b_base))
