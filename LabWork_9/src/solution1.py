from LabWork_9.src.utils import gen_matrix


def is_geometric(column: list):  # Визначаємо ф-цію що перевіряє чи є список геометричною послідовністю
    if len(column) <= 2:  # Перевіряємо чи список не менше 3 елементів
        return False

    if all([i == 0 for i in column]):  # Перевіряємо чи всі елементи списку є 0
        return True

    if column[0] == 0:  # Перевіряємо чи список не починається з 0
        return False

    q = column[1] / column[0]  # визначаємо відношення 2 елементу до 1
    for i in range(len(column)):  # йдемо по списку з кроком 1
        if i != 0:  # пропускаємо першу ітерацію
            if column[i - 1] * q != column[
                i]:  # перевіряємо чи добуток минулого елементу на різницю не є поточним елементом
                return False

    return True


def get_transposed_matrix(matrix: list[list]):  # Визначаємо ф-цію що транспонує матрицю
    return [list(row) for row in zip(*matrix)]  # розбиваємо матрицю на строки та перетворюємо їх в стовбці


def run_solution(matrix):
    g_matrix = matrix
    for col in get_transposed_matrix(g_matrix):
        print(col)
        return is_geometric(col)


if __name__ == "__main__":
    success = False
    while not success:
        run_solution(gen_matrix(10, 10))
