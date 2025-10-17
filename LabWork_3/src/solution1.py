class BirthDate:
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


if A == birthday.day:
    print("A == дню народження")
elif B == birthday.day:
    print("B == дню народження")
else:
    print("A і B не != дню народження")


if A == birthday.month:
    print("A == місяцю народження")
elif B == birthday.month:
    print("B == місяцю народження")
else:
    print("A і B не != місяцю народження")


if A == birthday.year:
    print("A == року народження")
elif B == birthday.year:
    print("B == року народження")
else:
    print("A і B != року народження")
