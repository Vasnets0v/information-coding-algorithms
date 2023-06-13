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


def hamming_encode(message):
    n = len(message)
    r = 0
    
    # Визначення кількості додаткових бітів (r)
    while 2**r < n + r + 1:
        r += 1
    
    # Створення кодового слова з нулями
    encoded_message = [0] * (n + r)
    
    # Запис вихідного повідомлення у кодове слово (зі зміщенням на додаткові біти)
    j = 0
    for i in range(n + r):
        if i + 1 == 2**j:
            j += 1
        else:
            encoded_message[i] = message[i - j]
    
    # Обчислення значень додаткових бітів
    for i in range(r):
        parity_bit_index = 2**i - 1
        parity_bit_value = 0
        
        for j in range(parity_bit_index, n + r, 2**(i + 1)):
            parity_bit_value ^= encoded_message[j]
        
        encoded_message[parity_bit_index] = parity_bit_value
    
    return encoded_message


def hamming_correct(encoded_message, error_position):
    r = 0
    
    # Визначення кількості додаткових бітів (r)
    while 2**r < len(encoded_message):
        r += 1
    
    # Знаходження позиції помилкового біту
    error_index = error_position - 1
    
    # Виправлення помилкового біту
    if encoded_message[error_index] == 0:
        encoded_message[error_index] = 1
    else:
        encoded_message[error_index] = 0
    
    # Обчислення значень додаткових бітів
    for i in range(r):
        parity_bit_index = 2**i - 1
        parity_bit_value = 0
        
        for j in range(parity_bit_index, len(encoded_message), 2**(i + 1)):
            parity_bit_value ^= encoded_message[j]
        
        if encoded_message[parity_bit_index] != parity_bit_value:
            # Знайдена помилка в додатковому біті
            error_index += parity_bit_index + 1
    
    if error_index < len(encoded_message):
        # Виправлення помилки в додатковому біті
        if encoded_message[error_index] == 0:
            encoded_message[error_index] = 1
        else:
            encoded_message[error_index] = 0
    
    return encoded_message


# текст повідомлення
data = "Хто хоче – шукає можливості, хто не хоче – шукає причини."
# повідомлення з помилкою в біті №3
corrupted_message = '00011001100101010100001100010111110000000100010001001010011101000101011011000110011001110100110101010011011001111000010111100110110100001100101001000110001000000001100010111100000001000100010010100111010010101101100011110011110101000111010011000010011111'

encoded_message, codes = shannon_fano_encode(data)

message = [int(bit) for bit in str(encoded_message)]  # Вхідне повідомлення
print('======')
print('Повідомлення закодоване алгоритмом Шенона-фано:\n', ''.join([str(elem) for elem in encoded_message]))

print('======')
encoded_message = hamming_encode(message)
print("Вхідне повідомлення з додаванням алгоритму Хеммінга:\n", ''.join([str(elem) for elem in encoded_message]))
print('======')
print('Пошкоджене повідомлення:\n', corrupted_message)
print('======')

#для роботи коду потрібно знати біт в якому знаходиться помилка
error_position = 3
corrected_message = hamming_correct([int(bit) for bit in corrupted_message], error_position)
print("Виправлене повідомлення:\n", ''.join([str(elem) for elem in corrected_message]))
print('======')
