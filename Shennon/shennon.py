# Вхідне повідомлення
from collections import Counter
from math import log2


message = "Хто хоче – шукає можливості, хто не хоче – шукає причини."
text_len = len(message) # довжина тексту


def get_statistic_about_text():

    statistic = dict(Counter(message))

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


def shannon_fano_encode(message):
    # Розрахунок ваг символів
    weights = {}
    for symbol in message:
        if symbol in weights:
            weights[symbol] += 1
        else:
            weights[symbol] = 1

    # Сортування символів за спаданням ваги
    symbols = sorted(weights.keys(), key=lambda s: -weights[s])

    # Рекурсивна функція для побудови кодових префіксів
    def build_code(prefix, symbols):
        if len(symbols) == 1:
            # Якщо залишився лише один символ, присвоюємо йому префікс
            codes[symbols[0]] = prefix
        else:
            # Розрахунок суми ваг символів
            total = sum(weights[s] for s in symbols)
            # Знаходження середнього значення суми ваг
            target = total / 2
            acc = 0
            for i, s in enumerate(symbols):
                acc += weights[s]
                if acc >= target:
                    # Розділення символів на дві групи зближених сум ваг
                    build_code(prefix + '0', symbols[:i+1])
                    build_code(prefix + '1', symbols[i+1:])
                    break

    # Створення пустого словника для збереження кодів символів
    codes = {}

    # Виклик рекурсивної функції для побудови кодових префіксів
    build_code('', symbols)

    # Кодування повідомлення за отриманими кодами символів
    encoded_message = ''.join(codes[s] for s in message)

    return encoded_message, codes


def shannon_fano_decode(encoded_message, codes):
    # Створення зворотного словника кодів символів
    reverse_codes = {v: k for k, v in codes.items()}

    decoded_message = ""
    current_code = ""
    for bit in encoded_message:
        current_code += bit
        if current_code in reverse_codes:
            decoded_message += reverse_codes[current_code]
            current_code = ""

    return decoded_message

print('=====')
# Кодування повідомлення
encoded_message, codes = shannon_fano_encode(message)
print("Encoded message:", encoded_message)
print("Codes:")
for symbol, code in codes.items():
    print(symbol, ":", code)

# Декодування повідомлення
decoded_message = shannon_fano_decode(encoded_message, codes)
print("Decoded message:", decoded_message)
print('кількість бітів, якими можна закодувати вхідне повідомлення:', len(encoded_message))
print('=====')

average_length = len(encoded_message)/len(message)
print('Середня довжина слів коду:', average_length)

# збитковість рахуємо за формулою (1 - (рівень ентропії/кількість біт) * 100%). В нашому випадку кількість біт = 6
before_compression = (1 - (get_entropy_level() / 6)) * 100
print('Коефіцієнт стиснення тексту до кодування:', before_compression, "%") 


after_compression = (1 - (get_entropy_level() / average_length)) * 100
print('Коефіцієнт стиснення тексту після кодування:', after_compression, "%")

print('=====')
print('Коефіцієнт ефективності:', before_compression - after_compression, '%')
print('=====')
