class Flight:
    number = "AA876"  # Номер рейсу
    airline = "airbus"  # Авіакомпанія
    departure_airport = "Istanbul Airport"  # Аеропорт вильоту
    departure_date = "3010"  # Дата вильоту (ddmm)
    departure_time = "2305"  # Час вильоту (hhmm)
    arrival_airport = "Chișinău Eugen Doga International Airport "  # Аеропорт прильоту
    arrival_date = "3110"  # Дата прильоту (ddmm)
    arrival_time = "0905"  # Час прильоту (hhmm)
    aircraft_model = "Airbus A320"  # Модель літака
    duration = 60  # Тривалість перельоту (Хв)


a1 = Flight()
a2 = Flight()
a3 = Flight()

a1.number = "LH1492"
a1.airline = "Lufthansa"
a1.departure_airport = "Frankfurt Airport"
a1.departure_date = "1510"
a1.departure_time = "1330"
a1.arrival_airport = "Boryspil International Airport"
a1.arrival_date = "1510"
a1.arrival_time = "1715"
a1.aircraft_model = "Airbus A320"
a1.duration = 105

a2.number = "TK1"
a2.airline = "Turkish Airlines"
a2.departure_airport = "Istanbul Airport"
a2.departure_date = "1610"
a2.departure_time = "0750"
a2.arrival_airport = "John F. Kennedy International Airport"
a2.arrival_date = "1610"
a2.arrival_time = "1150"
a2.aircraft_model = "Boeing 777-300ER"
a2.duration = 600

a3.number = "FR2436"
a3.airline = "Ryanair"
a3.departure_airport = "Warsaw Modlin Airport"
a3.departure_date = "1710"
a3.departure_time = "0620"
a3.arrival_airport = "Milan Bergamo Airport"
a3.arrival_date = "1710"
a3.arrival_time = "0835"
a3.aircraft_model = "Boeing 737-800"
a3.duration = 135

print("Екземпляр a1 класу Flight")
print("\tРейс", a1.number, "обслуговується компанією", a1.airline)
print("\tРейс бере початок в", a1.departure_airport, "о", a1.departure_time[:2:], "год", a1.departure_time[2::], "хв")
print("\t\tДата", a1.departure_date[:2:], "день", a1.departure_date[2::], "місяць")
print("\tТа прямує до", a1.arrival_airport, "о", a1.arrival_time[:2:], "год", a1.arrival_time[2::], "хв")
print("\t\tДата", a1.arrival_date[:2:], "день", a1.arrival_date[2::], "місяць")
print("\tЗаймає", a1.duration, "хв польоту на літаку", a1.aircraft_model)
print()

print("Екземпляр a2 класу Flight")
print("\tРейс", a2.number, "обслуговується компанією", a2.airline)
print("\tРейс бере початок в", a2.departure_airport, "о", a2.departure_time[:2:], "год", a2.departure_time[2::], "хв")
print("\t\tДата", a2.departure_date[:2:], "день", a2.departure_date[2::], "місяць")
print("\tТа прямує до", a2.arrival_airport, "о", a2.arrival_time[:2:], "год", a2.arrival_time[2::], "хв")
print("\t\tДата", a2.arrival_date[:2:], "день", a2.arrival_date[2::], "місяць")
print("\tЗаймає", a2.duration, "хв польоту на літаку", a2.aircraft_model)
print()

print("Екземпляр a3 класу Flight")
print("\tРейс", a3.number, "обслуговується компанією", a3.airline)
print("\tРейс бере початок в", a3.departure_airport, "о", a3.departure_time[:2:], "год", a3.departure_time[2::], "хв")
print("\t\tДата", a3.departure_date[:2:], "день", a3.departure_date[2::], "місяць")
print("\tТа прямує до", a3.arrival_airport, "о", a3.arrival_time[:2:], "год", a3.arrival_time[2::], "хв")
print("\t\tДата", a3.arrival_date[:2:], "день", a3.arrival_date[2::], "місяць")
print("\tЗаймає", a3.duration, "хв польоту на літаку", a3.aircraft_model)
