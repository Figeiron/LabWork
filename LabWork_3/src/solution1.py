class BirthDate:  # створимо клас для зрозумілішого запису дати народження
    def __init__(self, birthday_string: str):
        if len(birthday_string) != 8:
            raise ValueError

        self.birthday = birthday_string
        self.day = int(birthday_string[:2:])
        self.month = int(birthday_string[2:4:])
        self.year = int(birthday_string[4::])


while True:
    try:
        A = int(input("Введіть A: "))
        B = int(input("Введіть B: "))

        birthday = BirthDate(input("Введіть дату народження(ddmmyyyy):"))
        break

    except ValueError:
        print("Спробуйте знову")

if A == birthday.day:  # Перевіримо чи число A є днем народження
    print("A == дню народження")
else:
    print("A не != дню народження")

if B == birthday.day:  # Перевіримо чи число B є днем народження
    print("B == дню народження")
else:
    print("B не != дню народження")

if A == birthday.month:  # Перевіримо чи число A є місяцем народження
    print("A == місяцю народження")
else:
    print("A не != місяцю народження")

if B == birthday.month:  # Перевіримо чи число B є місяцем народження
    print("B == місяцю народження")
else:
    print("B не != місяцю народження")

if A == birthday.year: # Перевіримо чи число A є роком народження
    print("A == року народження")
else:
    print("A != року народження")

if B == birthday.year: # Перевіримо чи число B є роком народження
    print("B == року народження")
else:
    print("B != року народження")
