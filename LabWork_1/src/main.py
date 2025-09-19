def input_values():
    global a, b
    while True:
        try:
            a = float(input("Введіть a (a>0):"))
            b = float(input("Введіть b (b>0):"))
            break
        except ValueError:
            print("Спробуйте ще раз")

def solve_base_expression():
    global a, b
    try:
        c = (((a / b + 1) ** 2) / (a / b - b / a)) * \
            (((a ** 3 / b ** 3) - 1) / ((a ** 2 / b ** 2) + a / b + 1)) / \
            (((a ** 3 / b ** 3) + 1) / ((a ** 2 / b ** 2) - a / b + 1))
        print("Результат розвязання базового виразу: {}".format(c))
    except Exception as error:
        print("Виникла помилка: {}".format(error))

def solve_inverse_expression():
    global a, b
    try:
        c = (((a / b - 1) ** 2) / (a / b + b / a)) * \
            (((a ** 3 / b ** 3) + 1) / ((a ** 2 / b ** 2) - a / b - 1)) / \
            (((a ** 3 / b ** 3) - 1) / ((a ** 2 / b ** 2) + a / b - 1))
        print("Результат розвязання оберненого виразу: {}".format(c))
    except Exception as error:
        print("Виникла помилка: {}".format(error))

def solve_simplified_expression():
    global a, b
    try:
        c = a / b
        print("Результат розвязання спрощеного виразу: {}".format(c))
    except Exception as error:
        print("Виникла помилка: {}".format(error))

if __name__ == '__main__':
    input_values()
    solve_base_expression()
    solve_simplified_expression()
    solve_inverse_expression()