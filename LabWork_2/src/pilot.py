class Pilot:
    name = "Serhii"  # Імя
    surname = "Mykhailovych"  # Призвіще
    sex = "male"  # Стать
    corporate_email_address = "s.mykhailovych@airlinre.com"  # Адреса корпоративної пошти пілота
    license_number = "Gh439003"  # Номер ліцензії
    license_expiry_date = "05082030"  # Дата закінчення ліцензії (ddmmyyyy)
    birth_date = "15081980"  # Дата народження (ddmmyyyy)
    flight_number = 677  # Дата вильотів
    first_flight_date = "16022010"  # Дата першого вильоту (ddmmyyyy)
    base_airport = "Vinnytsia International Airport"  # Базовий аеропорт


a1 = Pilot()
a2 = Pilot()
a3 = Pilot()

a1.name = "Markus"
a1.surname = "Schneider"
a1.sex = "male"
a1.corporate_email_address = "m.schneider@lufthansa.com"
a1.license_number = "DE-LUF89342"
a1.license_expiry_date = "15062032"
a1.birth_date = "23071985"
a1.flight_number = 842
a1.first_flight_date = "12032009"
a1.base_airport = "Frankfurt Airport"

a2.name = "Ayşe"
a2.surname = "Demir"
a2.sex = "female"
a2.corporate_email_address = "a.demir@thy.com"
a2.license_number = "TR-TK55321"
a2.license_expiry_date = "01042031"
a2.birth_date = "07111988"
a2.flight_number = 1104
a2.first_flight_date = "05062012"
a2.base_airport = "Istanbul Airport"

a3.name = "Liam"
a3.surname = "O'Connor"
a3.sex = "male"
a3.corporate_email_address = "l.oconnor@ryanair.com"
a3.license_number = "IE-RYR67209"
a3.license_expiry_date = "30092033"
a3.birth_date = "21061990"
a3.flight_number = 756
a3.first_flight_date = "14052014"
a3.base_airport = "Dublin Airport"

print("Екземпляр a1 класу Pilot")
print("\tІмя та призвіще", a1.name, a1.surname)
print("\tСтать -", a1.sex)
print("\tОбслуговується в", a1.base_airport)
print("\tДата народження - ", a1.birth_date[:2:], a1.birth_date[2:4:], a1.birth_date[4::])
print("\tАдреса корп. пошти", a1.corporate_email_address)
print("\tНомер ліцензії", a1.license_number, ", дата закінчення - ", end="")
print(a1.license_expiry_date[:2:], a1.license_expiry_date[2:4:], a1.license_expiry_date[4::])
print("\tВиконав", a1.flight_number, "польотів, дата першого - ", end="")
print(a1.first_flight_date[:2:], a1.first_flight_date[2:4:], a1.first_flight_date[4::])
print()

print("Екземпляр a2 класу Pilot")
print("\tІмя та призвіще", a2.name, a2.surname)
print("\tСтать -", a2.sex)
print("\tОбслуговується в", a2.base_airport)
print("\tДата народження - ", a2.birth_date[:2:], a2.birth_date[2:4:], a2.birth_date[4::])
print("\tАдреса корп. пошти", a2.corporate_email_address)
print("\tНомер ліцензії", a2.license_number, ", дата закінчення - ", end="")
print(a2.license_expiry_date[:2:], a2.license_expiry_date[2:4:], a2.license_expiry_date[4::])
print("\tВиконав", a2.flight_number, "польотів, дата першого - ", end="")
print(a2.first_flight_date[:2:], a2.first_flight_date[2:4:], a2.first_flight_date[4::])
print()

print("Екземпляр a3 класу Pilot")
print("\tІмя та призвіще", a3.name, a3.surname)
print("\tСтать -", a3.sex)
print("\tОбслуговується в", a3.base_airport)
print("\tДата народження - ", a3.birth_date[:2:], a3.birth_date[2:4:], a3.birth_date[4::])
print("\tАдреса корп. пошти", a3.corporate_email_address)
print("\tНомер ліцензії", a3.license_number, ", дата закінчення - ", end="")
print(a3.license_expiry_date[:2:], a3.license_expiry_date[2:4:], a3.license_expiry_date[4::])
print("\tВиконав", a3.flight_number, "польотів, дата першого - ", end="")
print(a3.first_flight_date[:2:], a3.first_flight_date[2:4:], a3.first_flight_date[4::])
