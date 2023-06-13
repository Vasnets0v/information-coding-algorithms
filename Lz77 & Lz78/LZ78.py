def compress(data):
    dictionary, word = {0: ''}, 0
    dynamic_dictionary = lambda dictionary, key: dictionary.get(key) or dictionary.__setitem__(key, len(dictionary)) or 0
    result = []
    for char in data:
        token = (word, char)
        word = dynamic_dictionary(dictionary, token)
        if not word:
            result.append(token)
    result.append((word, ''))
    return result


def decompress(data):
    dictionary, j = {0: ''}, ''.join
    dynamic_dictionary = lambda dictionary, value: dictionary.__setitem__(len(dictionary), value) or value
    return j([dynamic_dictionary(dictionary, dictionary[codeword] + char) for (codeword, char) in data])


if __name__ == '__main__':
    data = "Хто хоче – шукає можливості, хто не хоче – шукає причини."
    compress_data = compress(data)
    decompress_data = decompress(compress_data)

    print('=====')
    print('Повідомлення:', data)
    print('=====')
    print('Закодоване повідомлення:', compress_data)
    print('=====')
    print('Декодоване повідомлення:', decompress_data)
    # У даному випадку, виходячи зі списку, кожен індекс може бути закодований з використанням 5 біт, оскільки у нас є 32 можливих значення для індексів (0-31).
    # Кількість біт для кодування символу 8
    print("Кількість біт необхідних для кодування повідомлення:", str((5 + 8) * len(compress_data))) 
    print('=====')
