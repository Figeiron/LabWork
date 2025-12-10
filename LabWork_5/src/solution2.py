while True:
    try:
        text = input("Введіть текст довжиною не менше 100 символів: ")
        K = int(input("Введіть ціле число K: "))

        if len(text) < 100:
            raise ValueError("Введено неправльний текст")

        break

    except ValueError as error:
        print(error)

count = 0  # ініціалізуємо змінну лічильник
for i in text.split(" "):  # створимо цикл для перебору слів у тексті
    if len(i) == K:  # перевіримо чи довжина слова == K
        count += 1  # додамо 1 до лічильника у випадку успіху

print("Кількість слів довжина яких == {}: ".format(K))
print(count)
