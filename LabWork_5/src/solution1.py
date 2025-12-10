while True:
    try:
        text = input("Введіть текст довжиною не менше 100 символів: ")

        if len(text) < 100:
            raise ValueError("Введено неправльний текст")

        break

    except ValueError as error:
        print(error)


def is_vowel(char: str):  # створимо ф-цію для перевірки на голосну літеру
    return char.lower() in set("aеєиіїоуюя")  # перевіримо чи належить символ множині голосних букв


text_not_vowel = ""  # ініціалізуємо змінну для запису форматованого тексту
for char in text:  # створимо цикл
    if not is_vowel(char):  # перевірка на голосну літеру
        text_not_vowel += char  # в випадку успіху додаємо символ

print("Заданий текст без голосних літер: ")
print(text_not_vowel)
