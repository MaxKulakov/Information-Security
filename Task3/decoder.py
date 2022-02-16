path_to_encoded_container = input('Введите путь до зашифрованного контейнера: ') \
                            or 'encoded_container.txt'

path_to_decoded_message = input('Введите путь до папки, в которую сохранить расшифрованное сообщение: ') \
                          + 'decoded_message.txt' or 'decoded_message.txt'

message = open(path_to_decoded_message, 'w', encoding='cp1251')
encoded_container = open(path_to_encoded_container, 'r', encoding='cp1251')


# Проходим посимвольно по зашифрованному контейнеру
# Если находим пробел, смотрим есть ли пробел за ним и если есть, то добавляем 1 в бинарную букву, иначе 0
# После этого при достижении размера бита преобразуем бинарный вид в символ и записываем в файл
# Если в контейнере после сообщения начинают идти пустые бинарные буквы, то заканчиваем расшифровку
end_of_file = False
binary_letter = ''
while not end_of_file:
    letter = encoded_container.read(1)
    if letter == ' ':
        letter = encoded_container.read(1)
        if letter == ' ':
            binary_letter += '1'
        else:
            binary_letter += '0'
    if len(binary_letter) == 8:
        if binary_letter == '00000000':
            break
        message.write(bytes([int(binary_letter, 2)]).decode('cp1251'))
        binary_letter = ''
    if not letter:
        end_of_file = True


message.close()
encoded_container.close()


print('Сообщение расшифровано')