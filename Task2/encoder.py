path_to_original_file = input('Введите путь до файла, информацию из которого нужно зашифровать: ') \
                        or 'original_message.txt'

path_to_original_container = input('Введите путь до контейнера, в котором нужно скрыть информацию: ') \
                             or 'original_container.txt'

path_to_encoded_container = input('Введите путь, куда сохранить контейнер: ') + 'encoded_container.txt' \
                            or 'encoded_container.txt'

message = open(path_to_original_file, 'r', encoding='cp1251').read()
container = open(path_to_original_container, 'r', encoding='cp1251')
encoded_container = open(path_to_encoded_container, 'w', encoding='cp1251')


# Получаем бинарную строку из сообщения, которое нужно зашифровать
# Для этого каждый байт сообщения преобразуем в бинарный вид,
# Убираем два первых символа и дополняем до длины 8 байт
# С помощью strip убираем лишние пробелы в начале и конце строки
binary_string = ''
bytes_of_message = message.encode('cp1251').strip()
for byte in bytes_of_message:
    binary_string += bin(byte)[2:].zfill(8)


# Считываем все строки изначального контейнера и записываем в зашифрованный контейнер
# Если байт бинарной строки равен 1, то дописываем в конец строки пробел
# Если байт не равен или если бинарная строка кончилась, то добавляем перенос
end_of_file = False
number_of_string = 0
while not end_of_file:
    file_line = container.readline().rstrip()
    encoded_container.write(file_line)
    if number_of_string < len(binary_string):
        if binary_string[number_of_string] == '1':
            encoded_container.write(' \n')
        else:
            encoded_container.write('\n')
    else:
        encoded_container.write('\n')
    number_of_string += 1
    if not file_line:
        end_of_file = True


container.close()
encoded_container.close()


print('Сообщение зашифровано')
input()