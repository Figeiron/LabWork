import re

while True:
    try:
        text = input("Введіть текст довжиною не менше 100 символів та не менше 3 речень (кінець речення \". \"): ")
        K = int(input("Введіть ціле число K: "))

        if len(text) < 100:
            raise ValueError("Введено менше 100 символів")

        if len(re.findall(r"\. ", text) + re.findall(r"\.$", text)) <= 3:
            raise ValueError("Введено менше 3 речень")

        break

    except ValueError as error:
        print(error)

count = 0  # ініціалізуємо змінну лічильник
for i in text.split(" "):  # створимо цикл для перебору слів у тексті
    if len(i) == K:  # перевіримо чи довжина слова == K
        count += 1  # додамо 1 до лічильника у випадку успіху

print("Кількість слів довжина яких == {}: ".format(K))
print(count)
