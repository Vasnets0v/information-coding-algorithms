text = 'Тільки нещасні вірять у владу долі. Щасливі світу цього приписують самим собі всі успіхи, яких вони досягають. – Джонатан Свіфт.'


# Кожен символ змінної ми теретворюємо в UICODE
def get_ascii_array_form_text():
    ascii = [ord(symbol) for symbol in text]

    return ascii


# перетворюємо UNICODE в текст
def get_text_form_ascii():
    text = ''
    ascii = get_ascii_array_form_text()

    for i in ascii:
        text += chr(i)

    return text


ascii_text = ''
for code in get_ascii_array_form_text():
    ascii_text += str(code) + ' '

print("=====")
print("Закодоване повідомлення за допомогою ASCII:", ascii_text)
print("=====")
print("Декодоване повідомлення з ASCII:", get_text_form_ascii())
print("=====")

# Оскільки українські символи зазвичай потребують 2 байти для кодування в UTF-8, 
# можемо припустити, що кожен символ кодується за допомогою 16 біт (2 байти).
# Таким чином, загальна кількість біт, необхідних для закодування вхідного повідомлення, дорівнює:

# 128 символів * 16 біт/символ = 2048 біт.
