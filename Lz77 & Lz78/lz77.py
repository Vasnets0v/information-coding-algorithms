def encode_lz77(message):
    encoded_message = []
    search_buffer_size = 10  # Розмір буфера пошуку
    look_ahead_buffer_size = 5  # Розмір буфера перегляду

    i = 0
    while i < len(message):
        search_start = max(0, i - search_buffer_size)
        search_end = i
        search_buffer = message[search_start:search_end]

        look_ahead_buffer = message[i:i + look_ahead_buffer_size]

        match_length = 0
        match_offset = 0

        for j in range(len(search_buffer), 0, -1):
            substring = search_buffer[j:]
            if look_ahead_buffer.startswith(substring):
                match_offset = len(search_buffer) - j
                match_length = len(substring)
                break

        if match_length == 0:
            encoded_message.append((0, 0, look_ahead_buffer[0]))
            i += 1
        else:
            encoded_message.append((match_offset, match_length, look_ahead_buffer[match_length]))
            i += match_length + 1

    return encoded_message


def decode_lz77(encoded_message):
    message = ""

    for triplet in encoded_message:
        match_offset, match_length, next_char = triplet

        if match_length == 0:
            message += next_char
        else:
            start_index = len(message) - match_offset
            for _ in range(match_length):
                message += message[start_index]
                start_index += 1

            message += next_char

    return message


message = "Хто хоче – шукає можливості, хто не хоче – шукає причини."
encoded = encode_lz77(message)
print('=====')
print('Повідомлення:', message)
print('=====')
print("Закодоване повідомлення:", encoded)
decoded = decode_lz77(encoded)
print('=====')
print("Декодоване повідомленя:", decoded)
print('=====')
# 1 біт для кодування позиції (у нашому випадку всі позиції дорівнюють 0, тому використовується 1 біт).
# 1 біт для кодування довжини (у нашому випадку всі довжини дорівнюють 0, тому використовується 1 біт).
# Кількість біт для кодування символу. В даному випадку, виходячи зі строки "Хто хоче – шукає можливості, хто не хоче – шукає причини", кожен символ може бути закодований з використанням 8 біт.
print("Кількість біт необхідних для кодування повідомлення:", str((1 + 1 + 8) * len(encoded)))
print('=====')
