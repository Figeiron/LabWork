import random

class Aircraft:
    model_id = 92384298  # Номер моделі
    rating = 1.2  # Рейтинг серед пасажирів
    seats_number = 168  # Кількість місць
    flight_range = 6940  # Дальність польоту (Км)
    wingspan = 34.09  # Розмах крила (М)
    length = 37.56  # Довжина (М)
    height = 11.76  # Висота (М)
    width = 4.4  # ширина (М)
    average_speed = 900  # Середня швидкість (Км/год)
    takeoff_speed = 250  # Швидкість зльоту (Км/год)

    def __repr__(self):
        return (
            f"Літак {self.model_id} з рейтингом у {self.rating}\n"
            f"Має {self.seats_number} місць та може літати на відстань до {self.flight_range} км\n"
            f"Злітає при швидкості {self.takeoff_speed} км/год, "
            f"з крейсерською швидкістю {self.average_speed} км/год\n"
            f"Габарити:\n"
            f"\tРозмах крил - {self.wingspan} м\n"
            f"\tДовжина - {self.length} м\n"
            f"\tВисота - {self.height} м\n"
            f"\tШирина - {self.width} м\n"
        )


aircraft_0 = Aircraft()
aircraft_1 = Aircraft()
aircraft_2 = Aircraft()
aircraft_3 = Aircraft()
aircraft_4 = Aircraft()

# Код з 8 знаків
aircraft_0.model_id = random.randint(10000000, 99999999)
aircraft_1.model_id = random.randint(10000000, 99999999)
aircraft_2.model_id = random.randint(10000000, 99999999)
aircraft_3.model_id = random.randint(10000000, 99999999)
aircraft_4.model_id = random.randint(10000000, 99999999)

# Число в діапазоні 1.0 - 5.0
aircraft_0.rating = random.randint(10, 50) / 10
aircraft_1.rating = random.randint(10, 50) / 10
aircraft_2.rating = random.randint(10, 50) / 10
aircraft_3.rating = random.randint(10, 50) / 10
aircraft_4.rating = random.randint(10, 50) / 10

# Число в діапазоні 1 - 200
aircraft_0.seats_number = random.randint(1, 200)
aircraft_1.seats_number = random.randint(1, 200)
aircraft_2.seats_number = random.randint(1, 200)
aircraft_3.seats_number = random.randint(1, 200)
aircraft_4.seats_number = random.randint(1, 200)

# Число в діапазоні 10 - 8000
aircraft_0.flight_range = random.randint(10, 8000)
aircraft_1.flight_range = random.randint(10, 8000)
aircraft_2.flight_range = random.randint(10, 8000)
aircraft_3.flight_range = random.randint(10, 8000)
aircraft_4.flight_range = random.randint(10, 8000)

# Залежить від к-кості місць
aircraft_0.wingspan = aircraft_0.seats_number * 0.25 + random.uniform(5, 10)
aircraft_1.wingspan = aircraft_0.seats_number * 0.25 + random.uniform(5, 10)
aircraft_2.wingspan = aircraft_0.seats_number * 0.25 + random.uniform(5, 10)
aircraft_3.wingspan = aircraft_0.seats_number * 0.25 + random.uniform(5, 10)
aircraft_4.wingspan = aircraft_0.seats_number * 0.25 + random.uniform(5, 10)

# Габарити мають залежність між один одним
aircraft_0.length = aircraft_0.wingspan * random.uniform(0.6, 0.9)
aircraft_1.length = aircraft_0.wingspan * random.uniform(0.6, 0.9)
aircraft_2.length = aircraft_0.wingspan * random.uniform(0.6, 0.9)
aircraft_3.length = aircraft_0.wingspan * random.uniform(0.6, 0.9)
aircraft_4.length = aircraft_0.wingspan * random.uniform(0.6, 0.9)

aircraft_0.height = aircraft_0.length * random.uniform(0.1, 0.2)
aircraft_1.height = aircraft_0.length * random.uniform(0.1, 0.2)
aircraft_2.height = aircraft_0.length * random.uniform(0.1, 0.2)
aircraft_3.height = aircraft_0.length * random.uniform(0.1, 0.2)
aircraft_4.height = aircraft_0.length * random.uniform(0.1, 0.2)

aircraft_0.width = 2.5 + aircraft_0.seats_number * 0.02
aircraft_1.width = 2.5 + aircraft_0.seats_number * 0.02
aircraft_2.width = 2.5 + aircraft_0.seats_number * 0.02
aircraft_3.width = 2.5 + aircraft_0.seats_number * 0.02
aircraft_4.width = 2.5 + aircraft_0.seats_number * 0.02

# Середня швидкість залежить від дальності польоту
aircraft_0.average_speed = int(300 + aircraft_0.flight_range * 0.05)
aircraft_1.average_speed = int(300 + aircraft_0.flight_range * 0.05)
aircraft_2.average_speed = int(300 + aircraft_0.flight_range * 0.05)
aircraft_3.average_speed = int(300 + aircraft_0.flight_range * 0.05)
aircraft_4.average_speed = int(300 + aircraft_0.flight_range * 0.05)

# Швидкість зльоту залежить від середньої
aircraft_0.takeoff_speed = int(aircraft_0.average_speed * random.uniform(0.55, 0.70))
aircraft_1.takeoff_speed = int(aircraft_0.average_speed * random.uniform(0.55, 0.70))
aircraft_2.takeoff_speed = int(aircraft_0.average_speed * random.uniform(0.55, 0.70))
aircraft_3.takeoff_speed = int(aircraft_0.average_speed * random.uniform(0.55, 0.70))
aircraft_4.takeoff_speed = int(aircraft_0.average_speed * random.uniform(0.55, 0.70))


print(aircraft_0)
print(aircraft_1)
print(aircraft_2)
print(aircraft_3)
print(aircraft_4)
