text = 'Тільки нещасні вірять у владу долі. Щасливі світу цього приписують самим собі всі успіхи, яких вони досягають. – Джонатан Свіфт.'

ascii = [ord(symbol) for symbol in text]


def decimal_to_bcd(n):

	if (n == 0):
		return ["0000"]

	rev = 0
	result = []

	while (n > 0):
		rev = rev * 10 + (n % 10)
		n = n // 10


	while (rev > 0):

		b = str(rev % 10)

		rev = rev // 10

		result.append("{0:04b}".format(int(b, 16)))

	return result


def bcd_to_decimal(s):
 
    length = len(s);
    check = 0;
    check0 = 0;
    num = 0;
    sum = 0;
    mul = 1;
    rev = 0;
     
    for i in range(length - 1, -1, -1):
         
        sum += (ord(s[i]) - ord('0')) * mul;
        mul *= 2;
        check += 1;
         
        if (check == 4 or i == 0):
            if (sum == 0 and check0 == 0):
                num = 1;
                check0 = 1;
                 
            else:
                 
                num = num * 10 + sum;
                 
            check = 0;
            sum = 0;
            mul = 1;
             
    while (num > 0):
        rev = rev * 10 + (num % 10);
        num //= 10;
         
    if (check0 == 1):
        return rev - 1;
         
    return rev;


def bcd_array(ascii):
    bcd = []

    for symbol in ascii:
        bcd_symbol = []

        for num in str(symbol):
            bcd_symbol.append(str(decimal_to_bcd(int(num))[0]))

        bcd.append(bcd_symbol)

    return bcd


def ascii_array(bcd_code):
	ascii = []

	for symbol in bcd_code:
		bit_str = ''

		for bit in symbol:
			bit_str += str(bcd_to_decimal(bit))

		ascii.append(int(bit_str))

	return ascii


def ascii_to_messange(ascii_cod):
    messange = ''
    for symbol in ascii_cod:
        messange += chr(symbol)

    return messange


bcd_code = bcd_array(ascii)

bcd_to_str = ''

for symbol in bcd_code:

	for bit in symbol:
		bcd_to_str += bit # + ' '
	
	# bcd_to_str += "| "

ascii_code = ascii_array(bcd_code)
message = ascii_to_messange(ascii_code)

print('=====')
print('Повідомлення:', text)
print('=====')
print('Закодоване повідомлення за допомогою BCD:', bcd_to_str)
print('=====')
print('декодоване повідомлення:', message)
print('=====')

# Оскільки BCD використовує 4 біти для представлення кожної десяткової цифри, 
# для кодування кожного цілого числа потрібно 4 * кількість десяткових цифр бітів. 
# Припустимо, що всі цілі числа мають розмір 3 десяткових цифр (наприклад, від 000 до 999).

# Кількість біт, необхідних для кодування одного цілого числа за допомогою BCD: 4 біти/десяткова цифра * 3 десяткові цифри = 12 біт.

# Загальна кількість біт, необхідних для закодування 128 цілих чисел за допомогою алгоритму BCD, дорівнює:

# 128 чисел * 12 біт/число = 1536 біт.

# ВИСНОВОК: результати будуть схожі
