class AirportBuilding:
    name = "Vinnytsia International Airport"  # Імя аеропорту
    type = "civilian"  # Тип аеропорту
    address = "Havryshivka"  # Адреса
    IATA_code = "VIN"  # Індивідуальний ідентифікатор
    UKWW_code = "ICAO"  # Міжнародний індивідуальний ідентифікатор
    altitude = 297  # Висота над рівнем моря
    runway_length = 2500  # Довжина злітної смуги
    opening_year = 1983  # Рік відкриття
    passenger_traffic = 489  # Пасажирообіг на останній актуальний рік
    area = 11000  # Площа аеропорту (Кв.м)


a1 = AirportBuilding()
a2 = AirportBuilding()
a3 = AirportBuilding()

a1.name = "Boryspil International Airport"
a1.type = "civilian"
a1.address = "Boryspil, Kyiv Oblast, Ukraine"
a1.IATA_code = "KBP"
a1.UKWW_code = "UKBB"
a1.altitude = 130
a1.runway_length = 4000
a1.opening_year = 1959
a1.passenger_traffic = 9400000
a1.area = 1500000

a2.name = "Heathrow Airport"
a2.type = "civilian"
a2.address = "Longford, Hounslow, London, United Kingdom"
a2.IATA_code = "LHR"
a2.UKWW_code = "EGLL"
a2.altitude = 25
a2.runway_length = 3902
a2.opening_year = 1946
a2.passenger_traffic = 62000000
a2.area = 1220000

a3.name = "Los Angeles International Airport"
a3.type = "civilian"
a3.address = "1 World Way, Los Angeles, California, USA"
a3.IATA_code = "LAX"
a3.UKWW_code = "KLAX"
a3.altitude = 38
a3.runway_length = 3682
a3.opening_year = 1930
a3.passenger_traffic = 66000000
a3.area = 1400000

print("Екземпляр a1 класу AirportBuilding")
print("\tАеропорт", a1.name, "знаходиться в", a1.address, "займає площу", a1.area, "км.кв")
print("\tІдентифікуєця як", a1.IATA_code, "за ідентифікатором IATA та", a1.UKWW_code, "за міжнародним кодом UWTT")
print("\tПочав функціювати у", a1.opening_year, "як", a1.type)
print("\tМає злітну смугу довжиною", a1.runway_length, "м яка знаходиться на", a1.altitude, "м над рівнем моря")
print("\tПропускає понад", a1.passenger_traffic, "людей на рік")
print()

print("Екземпляр a2 класу AirportBuilding")
print("\tАеропорт", a2.name, "знаходиться в", a2.address, "займає площу", a2.area, "км.кв")
print("\tІдентифікуєця як", a2.IATA_code, "за ідентифікатором IATA та", a2.UKWW_code, "за міжнародним кодом UWTT")
print("\tПочав функціювати у", a2.opening_year, "як", a2.type)
print("\tМає злітну смугу довжиною", a2.runway_length, "м яка знаходиться на", a2.altitude, "м над рівнем моря")
print("\tПропускає понад", a2.passenger_traffic, "людей на рік")
print()

print("Екземпляр a3 класу AirportBuilding")
print("\tАеропорт", a3.name, "знаходиться в", a3.address, "займає площу", a3.area, "км.кв")
print("\tІдентифікуєця як", a3.IATA_code, "за ідентифікатором IATA та", a3.UKWW_code, "за міжнародним кодом UWTT")
print("\tПочав функціювати у", a3.opening_year, "як", a3.type)
print("\tМає злітну смугу довжиною", a3.runway_length, "м яка знаходиться на", a3.altitude, "м над рівнем моря")
print("\tПропускає понад", a3.passenger_traffic, "людей на рік")
