#String variables
zvo = "ДонНУ імені Василя Стуса"                                # назва місця проведення занять
address = "вулиця 600-річчя, 21, Вінниця, Вінницька область"    # адреса місця проведення
group = "Б25"                                                   # назва групи
speciality = "F3"                                               # код спеціальності
speciality_title = "Комп’ютерні науки"                          # назва спеціальності

#int variables
postcode = 21000                                                # поштовий код місця проведення
subgroups_quantity = 3                                          # кількість підгруп
min_lessons_quantity = 1                                        # мінімальна к-ксть занять на день
max_lessons_quantity = 5                                        # максимальна к-ксть занять на день
days_with_first_lesson_quantity = 1                             # к-ксть днів з першим заняттям

#float variables
average_number_of_lessons_per_day = 2.5                         # середня к-ксть занять на день
ratio_lectures_to_practical = 0.6                               # відношення лекцій до практичних занять
lesson_duration = 1.33                                          # тривалість заняття
break_duration = 0.16                                           # тривалість перерви
ratio_lesson_to_break_duration = 8.3125                         # відношення тривалості заняття до перерви

print("Місце проведення:", zvo, ",", address, ",", postcode)
print("Класифікація розкладу:\n\tСпеціальність:", speciality_title, speciality,
      "\n\tГрупа:", group, "\n\tКількість підгруп:", subgroups_quantity)

print()

print("Класифікація занять:"
      "\n\tК-ксть днів з першим заняттям:", days_with_first_lesson_quantity,
      "\n\tМінімальна к-ксть:", min_lessons_quantity,
      "\n\tМаксимальна к-ксть:", max_lessons_quantity,
      "\n\tСередня к-ксть занять на день:", average_number_of_lessons_per_day,
      "\n\tВідношення лекцій до практичних занять:", ratio_lectures_to_practical,
      "\n\tТривалість заняття:", lesson_duration)

print()

print("Тривалість перерви:", break_duration)
print("Відношення тривалості заняття до перерви:", ratio_lesson_to_break_duration)