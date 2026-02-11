from pprint import pformat
from abc import ABC, abstractmethod
from enum import Enum, unique, auto


class TypeECTS(Enum):  # Визначаємо клас тип данних для оцінок за таблицею ECTS
    A = auto()
    B = auto()
    C = auto()
    D = auto()
    E = auto()
    FX = auto()

class SchemeECTS:  # Визначаємо клас контейнер для збереження схеми оцінювання
    def __init__(self, type_, **data):
        self.type = type_
        self.data = data

    def __repr__(self):
        return f"{self.type}: {self.data}"

@unique
class RatingECTS(Enum):  # Визначаємо клас що реєструє схеми оцінювання
    A = SchemeECTS(TypeECTS.A, threshold=90)
    B = SchemeECTS(TypeECTS.B, threshold=82)
    C = SchemeECTS(TypeECTS.C, threshold=75)
    D = SchemeECTS(TypeECTS.D, threshold=67)
    E = SchemeECTS(TypeECTS.E, threshold=60)
    FX = SchemeECTS(TypeECTS.FX, threshold=0)

class IRating(ABC):  # Визначаємо інтерфейс оцінки
    @property
    @abstractmethod
    def ECTS(self) -> SchemeECTS: # визначаємо абстрактний метод для оцінки за таблицею ECTS
        pass


class Rating(IRating):  # ініціалізуємо клас модель оцінки
    def __init__(self, numeric_rating: int):  # реалізовуємо метод конструктор для класу
        self.numeric = numeric_rating
        self._ects = self.__calc_ECTS_rating(self.numeric)  # задаємо оцінку за таблицею ECTS

    @property
    def ECTS(self) -> RatingECTS:
        return self._ects

    @staticmethod
    def __calc_ECTS_rating(numeric_rating: int):  # оголошуємо статичний метод для обрахунку оцінки за таблицею ECTS
        for ects in RatingECTS:  # йдемо по списку оцінки за ECTS та її порогу
            if numeric_rating >= ects.value.data["threshold"]:  # якщо задана оцінка >= порогу повертаємо її букву за таблицею ECTS
                return ects
        raise ValueError("Rating out of range")  # якщо оцінка залишилась не обробленою викидаємо помилку про її не відповідність заданим правилам

    def __repr__(self):  # реалізовуємо метод що визначає строкове визначення для обєкту оцінки
        return "rating: " + self.ECTS.name + " - " + str(self.numeric)


class RatingCounter:  # ініціалізуємо клас лічильник
    def __init__(self):  # реалізовуємо метод конструктор для класу
        self.table = {}  # ініціалізуємо хеш-таблицю для лічильника

    def __write_rating(self, rating: IRating):  # оголошуємо інкапсульований метод що визначає логіку при додаванні оцінки до лічильника
        self.table[rating.ECTS] = self.table.get(rating.ECTS, 0) + 1  # намагаємось отримати значення за ключем, якщо запис існує виконуємо +1 якщо ні то створюємо запис та встановлюємо значення на 0

    def add(self, rating: IRating):  # оголошуємо метод що визначає поведінку при додаванні оцінки до лічильника
        self.__write_rating(rating)

    def get_pretty_table(self):  # оголошуємо метод що повертає строкове визначення таблиці для обєкту лічильника
        return "\n".join([f"{ects.name}\t: {score}" for ects, score in list(self.table.items())])

    def __repr__(self):  # реалізовуємо метод що визначає строкове визначення для обєкту лічильника
        return pformat(self.table)


ratings = list(range(1, 101))  # ініціалізуємо заданий діапазон оцінок

if not ratings:  # перевірка на валідність діапазону
    raise ValueError("Ratings list not initialized")  # в разі хиибного діапазону викидаємо помилку

counter = RatingCounter()  # ініціалізуємо клас лічильник
for numeric_rating in ratings:  # йдемо по елементах діапазону
    counter.add(  # додаємо оцінку до лічильника
        Rating(numeric_rating)  # ініціалізуємо оцінку з заданого числа діапазону
    )

print(f"Таблиця підрахунку оцінок в діапазоні [{ratings[0]}; {ratings[-1]}]")
print(counter.get_pretty_table())
