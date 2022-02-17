path_to_encoded_container = input('Введите путь до зашифрованного контейнера: ') \
                            or 'encoded_container.txt'

path_to_decoded_message = input('Введите путь до папки, в которую сохранить расшифрованное сообщение: ') \
                          + 'decoded_message.txt' or 'decoded_message.txt'

message = open(path_to_decoded_message, 'w', encoding='cp1251')
encoded_container = open(path_to_encoded_container, 'r', encoding='cp1251')


# Проходим по всем строкам зашифрованномого контейнера
# Если последний символ строки является пробелом, то к переменной буквы добавляем 1, иначе 0
# После этого при достижении размера бита преобразуем бинарный вид в символ и записываем в файл
# Если в контейнере после сообщения начинают идти пустые бинарные буквы, то заканчиваем расшифровку
binary_letter = ''
end_of_file = False
while not end_of_file:
    file_line = encoded_container.readline().rstrip('\n')
    if file_line[-1] == ' ':
        binary_letter += '1'
    else:
        binary_letter += '0'
    if len(binary_letter) == 8:
        if binary_letter == '00000000':
            break
        message.write(bytes([int(binary_letter, 2)]).decode('cp1251'))
        binary_letter = ''
    if not file_line:
        end_of_file = True


encoded_container.close()
message.close()


print('Сообщение расшифровано')
input()