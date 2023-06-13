import heapq
from collections import Counter, defaultdict
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


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_frequency_table(message):
    frequency_table = defaultdict(int)
    for char in message:
        frequency_table[char] += 1
    return frequency_table


def build_huffman_tree(frequency_table):
    heap = []
    for char, freq in frequency_table.items():
        node = Node(char, freq)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)

        combined_freq = left_node.freq + right_node.freq
        combined_node = Node(None, combined_freq)
        combined_node.left = left_node
        combined_node.right = right_node

        heapq.heappush(heap, combined_node)

    return heap[0]


def build_huffman_codes(tree):
    huffman_codes = {}

    def build_codes(node, code):
        if node.char is not None:
            huffman_codes[node.char] = code
        else:
            build_codes(node.left, code + "0")
            build_codes(node.right, code + "1")

    build_codes(tree, "")
    return huffman_codes


def encode_message(message, huffman_codes):
    encoded_message = ""
    for char in message:
        encoded_message += huffman_codes[char]
    return encoded_message


def decode_message(encoded_message, huffman_tree):
    decoded_message = ""
    current_node = huffman_tree
    for bit in encoded_message:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_message += current_node.char
            current_node = huffman_tree

    return decoded_message


def main():

    frequency_table = build_frequency_table(message)
    huffman_tree = build_huffman_tree(frequency_table)
    huffman_codes = build_huffman_codes(huffman_tree)

    encoded_message = encode_message(message, huffman_codes)
    decoded_message = decode_message(encoded_message, huffman_tree)
    
    print('=====')
    print("Початкове повідомлення:", message)
    print("Закодоване повідомлення:", encoded_message)
    print("Розкодоване повідомлення:", decoded_message)
    print('=====')

    average_length = len(encoded_message)/len(message)
    print('Середня довжина слів коду:', average_length)

    before_compression = (1 - (get_entropy_level() / 6)) * 100
    print('Коефіцієнт стиснення тексту до кодування:', before_compression, "%")

    after_compression = (1 - (get_entropy_level() / average_length)) * 100
    print('Коефіцієнт стиснення тексту після кодування:', after_compression, "%")

    compression = before_compression - after_compression
    print('Коефіцієнт ефективності:', compression, '%')
    print('=====')
    print('Різниця в стисненні між алгоритмом Шенона-Фано і Хаффманом', compression - 27.696605316849045, '%')
    print('=====')


if __name__ == "__main__":
    main()
