import pprint
from pprint import pformat
from abc import ABC, abstractmethod
from enum import Enum, unique, auto
from dataclasses import dataclass
from random import randint


def gen_3d_dimension_massive(rows=10, cols=10, depth=10, min_n=0, max_n=7):
    return [
        [
            [
                randint(min_n, max_n)
                for _ in range(cols)]
            for _ in range(rows)]
        for _ in range(depth)]


class TypeBreed(Enum):
    rock_breed_soft = auto()
    rock_breed_hard = auto()
    rock_breed_super_hard = auto()
    water = auto()
    oil = auto()
    stone_coal = auto()
    iron_ore = auto()
    gold = auto()


@dataclass
class SchemeBreed:
    type: TypeBreed
    number: int
    profit: int

    def __repr__(self):
        return f"{self.type}"


@unique
class RegisterBreed(Enum):
    rock_breed_soft = SchemeBreed(TypeBreed.rock_breed_soft, 0, 0)
    rock_breed_hard = SchemeBreed(TypeBreed.rock_breed_hard, 1, 0)
    rock_breed_super_hard = SchemeBreed(TypeBreed.rock_breed_super_hard, 2, 0)
    water = SchemeBreed(TypeBreed.water, 3, 0)
    oil = SchemeBreed(TypeBreed.oil, 4, 1)
    stone_coal = SchemeBreed(TypeBreed.stone_coal, 5, 1)
    iron_ore = SchemeBreed(TypeBreed.iron_ore, 6, 2)
    gold = SchemeBreed(TypeBreed.gold, 7, 10)


class IBreed(ABC):
    @property
    @abstractmethod
    def type(self) -> RegisterBreed:
        pass


class Breed(IBreed):  # ініціалізуємо клас модель оцінки
    def __init__(self, number: int):  # реалізовуємо метод конструктор для класу
        self.number = number
        self._type = self.__assign_breed_scheme(self.number)  # задаємо оцінку за таблицею ECTS

    @property
    def type(self) -> RegisterBreed:
        return self._type

    @staticmethod
    def __assign_breed_scheme(number: int):
        for breed in RegisterBreed:
            if number == breed.value.number:
                return breed
        raise ValueError("Breed number out of range")

    def __repr__(self):
        return "breed: " + self.type.name + " - " + str(self.type.value.profit) + " - " + str(self.type.value.number)


class BreedExploration:
    def __init__(self, breed_map: list[list[list]]):
        self.breed_map = self.__calc_breed_map(breed_map)
        self.best_depth_col = 0

    def calc_column_profit(self, x, y):
        depth_column = self.__get_depth_col_list(x, y)
        return self.__calc_breed_list_profit(depth_column)

    def calc_best_column_profit(self):
        best_profit = 0
        col_cords = (0, 0)
        for y in range(len(self.breed_map[0])):
            for x in range(len(self.breed_map[0][0])):
                depth_column = self.__get_depth_col_list(x, y)
                profit = self.__calc_breed_list_profit(depth_column)
                if profit > best_profit:
                    best_profit = profit
                    col_cords = (x, y)
        return best_profit, col_cords

    @staticmethod
    def __calc_breed_map(breed_3d):
        for i in range(len(breed_3d)):
            for j in range(len(breed_3d[0])):
                for x in range(len(breed_3d[0][0])):
                    breed_3d[i][j][x] = Breed(breed_3d[i][j][x])
        return breed_3d

    def __get_depth_col_list(self, x, y):
        return [self.breed_map[j][x][y] for j in range(len(self.breed_map))]

    def __calc_breed_list_profit(self, breed_list: list):
        col_profit = 0
        for breed in breed_list:
            col_profit += breed.type.value.profit
        return col_profit

    def __repr__(self):
        return pformat(self.breed_map)


# ratings = list(range(1, 101))  # ініціалізуємо заданий діапазон оцінок

# if not ratings:  # перевірка на валідність діапазону
#     raise ValueError("Ratings list not initialized")  # в разі хиибного діапазону викидаємо помилку
#
# counter = RatingCounter()  # ініціалізуємо клас лічильник
# for numeric_rating in ratings:  # йдемо по елементах діапазону
#     counter.add(  # додаємо оцінку до лічильника
#         Rating(numeric_rating)  # ініціалізуємо оцінку з заданого числа діапазону
#     )
#
# print(f"Таблиця підрахунку оцінок в діапазоні [{ratings[0]}; {ratings[-1]}]")
# print(counter.get_pretty_table())


n = gen_3d_dimension_massive(depth=1, rows=2)
# e = BreedExploration(n)
# print(e)
# c = e.calc_best_column_profit()
# print(c)
pprint.pprint(n)