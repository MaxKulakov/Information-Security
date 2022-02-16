alphabet = [x for x in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя1234567890., ']


# Дополнение ключа до нужной длины
def key_fill(key, length):
    while len(key) < length:
        key += key
    return key[:length]


# Получаем сообщение и ключ и приводим к нижнему регистру
message = input('Введите зашиврованное сообщение (значение по умолчанию: тлй1яьащкщ 7пкг7щмкьшф4): ') or 'тлй1яьащкщ 7пкг7щмкьшф4'.lower()
key_word = input('Введите ключ шифрования (значение по умолчанию: ключ): ').lower() or 'ключ'.lower()

# Дополнение ключа до нужной длины
key_word = key_fill(key_word, len(message))


# Проходим по сообщению посимвольно и шифруем по формуле
decoded_message = ''
for i in range (0, len(message)):
    mj = alphabet.index(message[i])
    kj = alphabet.index(key_word[i])
    decoded_message += alphabet[(mj - kj) % len(alphabet)]


print('Расшифрованное сообщение: ' + decoded_message)
