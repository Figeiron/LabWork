class Aircraft:
    manufacturer = "airbus"  # Виробник
    model_name = "A320"  # Модель
    manufacturer_county = "France"  # Країна виробник
    seats_number = 168  # Кількість місць
    flight_range = 6940  # Дальність польоту (Км)
    wingspan = 34.09  # Розмах крила (М)
    length = 37.56  # Довжина (М)
    height = 11.76  # Висота (М)
    average_speed = 900  # Середня швидкість (Км/год)
    takeoff_speed = 250  # Швидкість зльоту (Км/год)


a1 = Aircraft()
a2 = Aircraft()
a3 = Aircraft()

a1.manufacturer = "Airbus"
a1.model_name = "A350-900"
a1.manufacturer_county = "France"
a1.seats_number = 350
a1.flight_range = 15000
a1.wingspan = 64.75
a1.length = 66.8
a1.height = 17.05
a1.average_speed = 905
a1.takeoff_speed = 260

a2.manufacturer = "Boeing"
a2.model_name = "737-800"
a2.manufacturer_county = "USA"
a2.seats_number = 189
a2.flight_range = 5436
a2.wingspan = 35.8
a2.length = 39.5
a2.height = 12.5
a2.average_speed = 842
a2.takeoff_speed = 255

a3.manufacturer = "Embraer"
a3.model_name = "E190"
a3.manufacturer_county = "Brazil"
a3.seats_number = 114
a3.flight_range = 4537
a3.wingspan = 28.72
a3.length = 36.24
a3.height = 10.57
a3.average_speed = 829
a3.takeoff_speed = 240

print("Екземпляр a1 класу Aircraft")
print("\tЛітак", a1.manufacturer, a1.model_name, "вироблений у", a1.manufacturer_county)
print("\tМає", a1.seats_number, "місць та може літати на відстань до", a3.flight_range, "км")
print("\tЗлітає при швидкості", a1.takeoff_speed, "Км/год, з крейсерською швидкістю", a1.average_speed, "км/год")
print("\tГабарити:\n\tРозмах крил -", a1.wingspan, "м")
print("\t\tДовжина -", a1.length, "м")
print("\t\tВисота -", a1.height, "м")
print()

print("Екземпляр a2 класу Aircraft")
print("\tЛітак", a2.manufacturer, a2.model_name, "вироблений у", a2.manufacturer_county)
print("\tМає", a2.seats_number, "місць та може літати на відстань до", a3.flight_range, "км")
print("\tЗлітає при швидкості", a2.takeoff_speed, "Км/год, з крейсерською швидкістю", a2.average_speed, "км/год")
print("\tГабарити:\n\tРозмах крил -", a2.wingspan, "м")
print("\t\tДовжина -", a2.length, "м")
print("\t\tВисота -", a2.height, "м")
print()

print("Екземпляр a3 класу Aircraft")
print("\tЛітак", a3.manufacturer, a3.model_name, "вироблений у", a3.manufacturer_county)
print("\tМає", a3.seats_number, "місць та може літати на відстань до", a3.flight_range, "км")
print("\tЗлітає при швидкості", a3.takeoff_speed, "Км/год, з крейсерською швидкістю", a3.average_speed, "км/год")
print("\tГабарити:\n\tРозмах крил -", a3.wingspan, "м")
print("\t\tДовжина -", a3.length, "м")
print("\t\tВисота -", a3.height, "м")
