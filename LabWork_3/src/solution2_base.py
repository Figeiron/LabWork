while True:
    try:
        variables = []

        for i in range(5):
            variables.append(int(input("Введіть значення для x{}: ".format(i + 1))))
        break

    except ValueError:
        print("Спробуйте знову")

count = 0

for i in range(5):
    for j in range(5):
        if i != j and variables[j] != 0:
            if variables[i] % variables[j] == 0:
                count += 1

print(count, "чисел, є дільниками інших чисел массиву")