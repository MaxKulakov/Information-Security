letter_map = {'с': 'c', 'е': 'e', 'о': 'o', 'А': 'A',
              'В': 'B', 'С': 'C', 'Е': 'E', 'Н': 'H',
              'М': 'M', 'О': 'O', 'Р': 'P', 'Т': 'T',
              'Х': 'X'}


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
# С помощью strip убираем лишние пробелы в начале и конце строки
binary_string = ''
bytes_of_message = message.encode('cp1251').strip()
for byte in bytes_of_message:
    binary_string += bin(byte)[2:].zfill(8)


# Сравниваем каждую букву контейнера с словарём и если байт сообщения = 1
# И предыдущее условие выполнено, то производим замену одного символа на другой
number_of_space = 0
for letter in container:
    if number_of_space < len(binary_string):
        if letter in letter_map.keys():
            if binary_string[number_of_space] == '1':
                encoded_container.write(letter_map.get(letter))
            else:
                encoded_container.write(letter)
            number_of_space += 1
        else:
            encoded_container.write(letter)
    else:
        encoded_container.write(letter)


encoded_container.close()


print('Сообщение зашифровано')
input()