path_to_original_file = input('Введите путь до файла, информацию из которого нужно зашифровать: ') \
                        or 'original_message.txt'

path_to_original_container = input('Введите путь до контейнера, в котором нужно скрыть информацию: ') \
                             or 'original_container.txt'

path_to_encoded_container = input('Введите путь, куда сохранить контейнер: ') + 'encoded_container.txt' \
                            or 'encoded_container.txt'

message = open(path_to_original_file, 'r', encoding='cp1251').read()
container = open(path_to_original_container, 'r', encoding='cp1251').read()
encoded_container = open(path_to_encoded_container, 'w', encoding='cp1251')


# Получаем бинарную строку из сообщения, которое нужно зашифровать
# Для этого каждый байт сообщения преобразуем в бинарный вид,
# Убираем два первых символа и дополняем до длины 8 байт
binary_string = ''
bytes_of_message = message.encode('cp1251')
for byte in bytes_of_message:
    binary_string += bin(byte)[2:].zfill(8)


# Для каждого символа контейнера смотрим на наличие пробела
# Если найден пробел в контейнере и изначальное сообщение ещё не окончено
# Если байт сообщения равен 1 то удваиваем пробел, иначе оставляем как есть
# После окончания байтов сообщения дописываем контейнер до конца
number_of_space = 0
for letter in container:
    if letter != ' ':
        encoded_container.write(letter)
    else:
        if number_of_space < len(binary_string):
            if binary_string[number_of_space] == '1':
                encoded_container.write('  ')
            else:
                encoded_container.write(' ')
        number_of_space += 1
    if letter == ' ' and number_of_space > len(binary_string):
        encoded_container.write(letter)


encoded_container.close()


print('Сообщение зашифровано')