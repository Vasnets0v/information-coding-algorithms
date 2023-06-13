from collections import Counter
from math import log2

import openpyxl


text = 'Хто хоче – шукає можливості, хто не хоче – шукає причини.'
alphabet_len = 33 # потужність алфавіту
text_len = len(text) # довжина тексту
info_per_symbol = log2(alphabet_len) # кількість інформації на один символ в бітах. По формулі N = 2 ^ i
amout_info = info_per_symbol * text_len # кількість інформації на повідомлення


def get_statistic_about_text():

    statistic = dict(Counter(text))

    return sorted(statistic.items(), key=lambda x:x[1], reverse=True)


# визначеємо шанс появи окремиї символів в тексті, де символ в тексті \ кількість всіх символів
def get_occurrence_probability():
    statistic = get_statistic_about_text()

    occurrence_probability = {}
    for symbol in statistic:
        occurrence_probability[symbol[0]] = symbol[1] / text_len

    return occurrence_probability


# рівень ентропії за формулою де x - це всі символи тесту. сума -(P(x) * log2(P(x)))
def get_entropy_level():
    entropy = 0
    occurrence_probability = get_occurrence_probability()

    for symbol in occurrence_probability:
        entropy -= occurrence_probability[symbol] * log2(occurrence_probability[symbol])

    return entropy


def create_exel_book():
    book = openpyxl.Workbook()
    sheet = book.active
    sheet.title = "lab1"

    sheet['A1'] = 'Символ'
    sheet['B1'] = 'Частота появи'

    statistic = get_statistic_about_text()

    for table in book.worksheets:
        for row in statistic:
            table.append(row)

    book.save("lab2.xlsx")

print("=====")
print('Повідомлення:', text)
print("=====")
print("Потужність алфавіту", alphabet_len)
print("Кількісь символів в повідомлені", text_len)
print("Інформації на символ", info_per_symbol, "бит")
print("Інформації в повідомленні", amout_info, "бит")
print('Рівень ентропії', get_entropy_level())
print("=====")

num = 0
statistic = get_statistic_about_text()
for i in statistic:
    print(i[0], " - ", i[1])
    num += i[1]
print("Загальна кількість символів (перевірка)", num)

print("=====")
create_exel_book()