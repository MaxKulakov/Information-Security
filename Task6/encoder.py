import os

path_to_directory = input('Введите путь до директории (folder-with-files по умолчанию): ') \
                        or 'folder-with-files'
key_word = input('Введите ключ шифрования (значение по умолчанию: ключ): ').lower() or 'ключ'.lower()
path_to_archive = input('Введите путь, куда сохранить архив: ') + 'directory.archive' \
                  or 'directory.archive'

archive = open(path_to_archive, 'wb')


# Получаем список всех файлов во всех директориях
os.chdir(path_to_directory)
path_to_files = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        path_to_files.append(os.path.join(root, name))


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

archive.write((path_to_directory + '\n').encode())
first_line = True
for x in path_to_files:
    with open(x, 'rb') as path:
        file = path.read()
        if not first_line:
            archive.write(('\n').encode())
        else:
            first_line = False
        st = ('*****file*****\n' + x + '\n').encode()
        archive.write(st)
        archive.write(file)

archive.close()


def encoderFile(file):
    encoded_archive = []
    for i in range(0, len(file)):
        fi = file[i]
        mj = alphabet.index(str(fi).encode())
        ki = key_word[i]
        kj = alphabet.index(str(ki).encode())
        enc = alphabet[(mj + kj) % len(alphabet)]
        encoded_archive.append(enc)
    return b''.join(encoded_archive)


#шифруем архив
os.chdir('..')
with open(path_to_archive, 'rb') as path:
    file = path.read()

    key_word = key_fill(key_word.encode(), len(file))

    enc_bytes = encoderFile(file)

with open(path_to_archive, 'wb') as path:
    path.write(encoderFile(file))
