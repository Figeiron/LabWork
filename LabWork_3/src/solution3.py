def str_to_list(num):
    return list(map(lambda x: int(x), list(num)))


while True:
    try:
        A = input("Введіть A: ")
        B = input("Введіть B: ")

        a_base = max(str_to_list(A)) + 1
        b_base = max(str_to_list(B)) + 1
        break

    except ValueError:
        print("Спробуйте знову")

print(a_base)
print(b_base)

print(int(A, a_base))
print(int(B, b_base))
