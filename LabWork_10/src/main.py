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
class RegisteredBreed(Enum):
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
    def type(self) -> RegisteredBreed:
        pass


class Breed(IBreed):
    def __init__(self, number: int):
        self.number = number
        self._type = self.__assign_breed_scheme(self.number)

    @property
    def type(self) -> RegisteredBreed:
        return self._type

    @staticmethod
    def __assign_breed_scheme(number: int):
        for breed in RegisteredBreed:
            if number == breed.value.number:
                return breed
        raise ValueError("Breed number out of range")

    def __repr__(self):
        return "breed: " + self.type.name + " - " + str(self.type.value.profit) + " - " + str(self.type.value.number)


class BreedExploration:
    def __init__(self, breed_map: list[list[list]]):
        self.breed_map = self.__calc_breed_map(breed_map)

    @staticmethod
    def __calc_breed_map(breed_3d):
        return [
            [
                [Breed(breed_3d[d][x][y]) for y in range(len(breed_3d[0][0]))]
                for x in range(len(breed_3d[0]))
            ]
            for d in range(len(breed_3d))
        ]

    def __repr__(self):
        return pformat(self.breed_map)


@dataclass
class BreedColumn:
    x: int
    y: int
    breed_list: list[RegisteredBreed]

    @staticmethod
    def __calc_breed_list_profit(breed_list):
        return sum(breed.type.value.profit for breed in breed_list)

    @property
    def profit(self):
        return self.__calc_breed_list_profit(self.breed_list)

    @property
    def pos(self):
        return (self.x, self.y)

    def __iter__(self):
        return iter(self.breed_list)


class BreedDepthExploration(BreedExploration):
    def __init__(self, breed_map: list[list[list]]):
        super().__init__(breed_map)

        self.breed_columns = self.__get_columns()

    def __get_column(self, x, y):
        breeds = []
        for i in range(len(self.breed_map)):
            breed = self.breed_map[i][x][y]
            breeds.append(breed)
        return BreedColumn(x,y, breeds)

    def __get_columns(self):
        column = []
        for x in range(len(self.breed_map[0])):
            for y in range(len(self.breed_map[0][0])):
                column.append(self.__get_column(x, y))

        return column


    def get_best_profit_column(self):
        best_column = self.breed_columns[0]
        for column in self.breed_columns:
            if column.profit > best_column.profit:
                best_column = column
        return best_column


b_m = gen_3d_dimension_massive()
exp = BreedDepthExploration(b_m)
print(exp.get_best_profit_column().profit)
