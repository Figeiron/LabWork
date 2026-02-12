import random


def array_gen(length=10):  # Для прикладу визначаємо ф-цію для генерацї випадкових массивів заданої довжини
    return [random.randint(0, 100) for _ in range(length)]


def find_min(array: list):  # Визначає ф-цію пошуку мінімального елементу массиву
    min_i = array[0]  # Вважаємо перший елемент мінімальний
    for i in array:  # Йдемо по елементах списку
        if i < min_i:
            min_i = i  # Якщо елемент менший за минулий мінімальний вважаємо його мінімальним
    return min_i


def find_max(array: list):  # Визначає ф-цію пошуку максимального елементу массиву
    max_i = array[0]  # Вважаємо перший елемент максимальний
    for i in array:
        if i > max_i:
            max_i = i  # Якщо елемент менший за минулий максимальний вважаємо його мінімальним
    return max_i


example_array = array_gen()

if not example_array:
    raise ValueError("Array is not initialized")  # Викидаємо по милку у разі не валідного массиву

max_of_array = find_max(example_array)
min_of_array = find_min(example_array)

print(f"Початковий массив: {example_array}")
print(f"Мінімальний елемент: {min_of_array}")
print(f"Максимальнй елемент: {max_of_array}")

example_array.remove(max_of_array)
example_array.remove(min_of_array)

print(f"Початковий массив після видаленняЖ {example_array}")
