def str_to_digit_list(num):
    return list(map(int, list(num)))


while True:
    try:
        A = input("Введіть A: ")
        B = input("Введіть B: ")

        a_base = max(str_to_digit_list(A)) + 1
        b_base = max(str_to_digit_list(B)) + 1
        break

    except ValueError:
        print("Спробуйте знову")

print("Мінімально можлива числення для числа А:", a_base)
print("Мінімально можлива числення для числа В:", b_base)

print("Число А в десятковій системі:", int(A, a_base))
print("Число В в десятковій системі:", int(B, b_base))
