import os


key_word = input('Введите ключ шифрования (значение по умолчанию: ключ): ').lower() or 'ключ'.lower()
path_to_archive = input('Введите путь, куда сохранить архив: ') + 'directory.archive' \
                  or 'directory.archive'


def getAlphabet():
    alphabet = []
    for i in range (0, 256):
        alphabet.append(str(i).encode())
    return alphabet

def key_fill(key, length):
    key_byte_list = list(key)
    while len(key_byte_list) < length:
        key_byte_list += key_byte_list
    return bytes(key_byte_list[:length])



alphabet = getAlphabet()



def decoderFile(file):

    decoded_archive = []
    for i in range(0, len(file)):
        fi = file[i]
        mj = alphabet.index(str(fi).encode())
        ki = key_word[i]
        kj = alphabet.index(str(ki).encode())
        enc = alphabet[(mj - kj) % len(alphabet)]
        decoded_archive.append(enc)
    return b''.join(decoded_archive)



#шифруем архив
# os.chdir('..')
with open(path_to_archive, 'rb') as path:
    file = path.read()
    key_word = key_fill(key_word.encode(), len(file))

    # print(file)
    print(decoderFile(file).decode('UTF-8'))


    # dec_bytes = decoderFile(file)
    # print(''.join(decoderFile(file)).decode('utf-8'))

# with open(path_to_archive, 'wb') as path:
#     path.write(encoderFile(file))
