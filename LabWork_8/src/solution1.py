from pprint import pformat

from pyparsing import countedArray

ratings = list(range(0, 101))

if not ratings:
    raise ValueError


class Rating:
    ratings_table = {
        "A": 90,
        "B": 82,
        "C": 75,
        "D": 67,
        "E": 60,
        "FX": 0,
    }

    def __init__(self, numeric_rating: int):
        self.numeric = numeric_rating
        self.ECTS = Rating.__calc_ECTS_rating(self.numeric)

    def __repr__(self):
        return "rating: " + self.ECTS + " - " + str(self.numeric)

    @staticmethod
    def __calc_ECTS_rating(numeric_rating: int):
        for ECTS, numeric in Rating.ratings_table.items():
            if numeric <= numeric_rating:
                return ECTS


class RatingCounter:
    def __init__(self):
        self.ratings_count = {}

    def __write_rating(self, rating: Rating):
        if not rating.ECTS in self.ratings_count.keys():
            self.ratings_count[rating.ECTS] = 1
        else:
            self.ratings_count[rating.ECTS] += 1

    def add(self, rating: Rating):
        self.__write_rating(rating)

    def clear(self):
        self.ratings_count = {}

    def __repr__(self):
        pformat(self.ratings_count)


counter = RatingCounter
for rating_n in ratings:
    rating = Rating(rating_n)
    counter.add(rating)
print(counter)
