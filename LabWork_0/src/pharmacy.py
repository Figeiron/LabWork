#String variables
title = "АНЦ"                                   # назва аптеки
address = "проспект Повітряних Сил, 50/2, Київ" # адреса аптеки
website = "www.example-pharmacy.ua"             # веб-сайт аптеки
phone_number = "+380070738084"                  # моб. телефон аптеки
owner = "Костянтин Пучин"                       # власник аптеки

#int variables
outlets_quantity = 963                          # к-ксть торгових точок
clients_quantity = 6000000                      # к-ксть клієнтів
number_of_towns = 135                           # к-ксть населених пунктів
start_year = 2000                               # рік заснування
product_item_count = 2376                       # к-ксть позицій товару

#float variables
market_share = 14.01                            # доля ринку у %
average_items_per_receipt = 2.1                 # середня кількість товарів у чеку
rating = 4.5                                    # рейтинг аптеки (1-5)
average_price_per_item = 205.19                 # середня ціна за позицію (грн)
profit_per_year = 1.557                         # прибуток за рік (млрд грн)

print("Назва аптеки:", title)
print("Адреса:", address)
print("Веб-сайт:", website)
print("Моб. телефон:", phone_number)
print("Власник:", owner)

print()

print("Заснована в:", start_year)
print("Кількість торгових точок:", outlets_quantity)
print("Кількість клієнтів:", clients_quantity)
print("Кількість населених пунктів:", number_of_towns)
print("Кількість товарних позицій:", product_item_count)

print()

print("Доля ринку:", market_share, "%")
print("Середня кількість товарів у чеку:", average_items_per_receipt)
print("Рейтинг аптеки:", rating, "/5")
print("Середня ціна за позицію:", average_price_per_item, "грн")
print("Прибуток за рік:", profit_per_year, "млрд грн")