while True:
    try:
        variables = []

        for i in range(5):
            variables.append(int(input("Введіть значення для x{}: ".format(i + 1))))

        x1 = variables[0]
        x2 = variables[1]
        x3 = variables[2]
        x4 = variables[3]
        x5 = variables[4]

        break

    except ValueError:
        print("Спробуйте знову")

count = 0  # ініціалізуємо змінну лічильник

if x1 != 0:  # Перевіряємо чи можливе ділення
    if x2 % x1 == 0: # Перевіряємо чи ділення без остачі можливе
        count += 1 # Додаємо 1
    if x3 % x1 == 0:
        count += 1
    if x4 % x1 == 0:
        count += 1
    if x5 % x1 == 0:
        count += 1

if x2 != 0:  # Перевіряємо чи можливе ділення
    if x1 % x2 == 0:
        count += 1
    if x3 % x2 == 0:
        count += 1
    if x4 % x2 == 0:
        count += 1
    if x5 % x2 == 0:
        count += 1

if x3 != 0:  # Перевіряємо чи можливе ділення
    if x1 % x3 == 0:
        count += 1
    if x2 % x3 == 0:
        count += 1
    if x4 % x3 == 0:
        count += 1
    if x5 % x3 == 0:
        count += 1

if x4 != 0:  # Перевіряємо чи можливе ділення
    if x1 % x4 == 0:
        count += 1
    if x2 % x4 == 0:
        count += 1
    if x3 % x4 == 0:
        count += 1
    if x5 % x4 == 0:
        count += 1

if x5 != 0:  # Перевіряємо чи можливе ділення
    if x1 % x5 == 0:
        count += 1
    if x2 % x5 == 0:
        count += 1
    if x3 % x5 == 0:
        count += 1
    if x4 % x5 == 0:
        count += 1

print(count, "чисел, є дільниками інших чисел")
