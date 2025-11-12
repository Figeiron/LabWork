while True:
    print("Введіть два дійсні числа, А < B")
    try:
        A = int(input("Введіть A: "))
        B = int(input("Введіть B: "))

        if not A < B:
            raise ValueError

        break

    except ValueError:
        print("Спробуйте знову")

AB_product = A * B  # Знаходимо добуток A та B
count = 0  # ініціалізуємо змінну лічильник

for i in range(A, B + 1):  # Створюємо цикл для перебору всіх значень в діапазоні (0; B]
    if i != 0 and AB_product % i == 0:  # перевіряємо дільники числа AB_product
        count += 1  # додаємо 1 в випадку успішного ділення

print(f"У діапазоні [{A}, {B}] {count} чисел є діьниками {AB_product}")
