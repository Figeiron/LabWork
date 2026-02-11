from pprint import pformat


class Rating:  # ініціалізуємо клас модель оцінки
    table = [  # задаємо порядок та пороги оцінок за таблицею ECTS
        ("A", 90),
        ("B", 82),
        ("C", 75),
        ("D", 67),
        ("E", 60),
        ("FX", 0)
    ]

    def __init__(self, numeric_rating: int):  # реалізовуємо метод конструктор для класу
        self.numeric = numeric_rating
        self.ECTS = self.__calc_ECTS_rating(self.numeric)  # задаємо оцінку за таблицею ECTS

    @staticmethod
    def __calc_ECTS_rating(numeric_rating: int):  # оголошуємо статичний метод для обрахунку оцінки за таблицею ECTS
        for ECTS, threshold in Rating.table:  # йдемо по списку оцінки за ECTS та її порогу
            if numeric_rating >= threshold:  # якщо задана оцінка >= порогу повертаємо її букву за таблицею ECTS
                return ECTS
        raise ValueError("Rating out of range")  # якщо оцінка залишилась не обробленою викидаємо помилку про її не відповідність заданим правилам

    def __repr__(self):  # реалізовуємо метод що визначає строкове визначення для обєкту оцінки
        return "rating: " + self.ECTS + " - " + str(self.numeric)


class RatingCounter:
    def __init__(self):  # реалізовуємо метод конструктор для класу
        self.table = {}  # ініціалізуємо хеш-таблицю для лічильника

    def __write_rating(self, rating: Rating):  # оголошуємо інкапсульований метод що визначає логіку при додаванні оцінки до лічильника
        self.table[rating.ECTS] = self.table.get(rating.ECTS, 0) + 1  # намагаємось отримати значення за ключем, якщо запис існує виконуємо +1 якщо ні то створюємо запис та встановлюємо значення на 0

    def add(self, rating: Rating):  # оголошуємо метод що визначає поведінку при додаванні оцінки до лічильника
        self.__write_rating(rating)

    def get_pretty_table(self):  # оголошуємо метод що повертає строкове визначення таблиці для обєкту лічильника
        return "\n".join([f"{ECTS_rating}\t: {score}" for ECTS_rating, score in list(self.table.items())[::-1]])

    def __repr__(self):  # реалізовуємо метод що визначає строкове визначення для обєкту лічильника
        return pformat(self.table)


ratings = list(range(0, 101))  # ініціалізуємо заданий діапазон оцінок

if not ratings:  # перевірка на валідність діапазону
    raise ValueError("Ratings list not initialized")  # в разі хиибного діапазону викидаємо помилку

counter = RatingCounter()  # ініціалізуємо клас лічильник
for numeric_rating in ratings:  # йдемо по елементах діапазону
    counter.add(  # додаємо оцінку до лічильника
        Rating(numeric_rating)  # ініціалізуємо оцінку з заданого числа діапазону
    )

print(f"Таблиця підрахунку оцінок в діапазоні [{ratings[0]}; {ratings[-1]}]")
print(counter.get_pretty_table())
