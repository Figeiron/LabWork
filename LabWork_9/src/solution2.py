from LabWork_9.src.utils import gen_matrix
from pprint import pprint


def sort(numbers):  # Реалізуємо ф-цію сортування методом бульбашки
    n = len(numbers)
    for i in range(n):  # Йдемо з кроком 1
        for j in range(n - i):  # Йдемо з кроком 1
            if j != 0:  # пропускаємо першу ітерацію
                if numbers[j - 1] > numbers[j]:  # якщо минулий елемент більше за теперішній
                    numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]  # міняємо їх місцями
    return numbers


def get_transposed_matrix(matrix: list[list]):  # Визначаємо ф-цію що транспонує матрицю
    return [list(row) for row in zip(*matrix)]  # розбиваємо матрицю на строки та перетворюємо їх в стовбці


def sort_matrix_rows(matrix: list[list]):  # Визначаємо ф-цію що сортує кожен рядок матриці
    sorted_matrix = []
    for i in range(len(matrix)):
        sorted_matrix.append(sort(matrix[i]))
    return sorted_matrix


def run_solution(matrix):
    sorted_rows_matrix = sort_matrix_rows(matrix)
    transposed_matrix = get_transposed_matrix(sorted_rows_matrix)
    sorted_matrixx = sort_matrix_rows(transposed_matrix)

    pprint(sorted_matrixx)

if __name__ == '__main__':
    run_solution(gen_matrix(rows=10, cols=10))


