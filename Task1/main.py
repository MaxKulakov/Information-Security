import os
import mmap

offset = int(input('Введите сдвиг (16 по умолчанию): ') or 16)
signature_size = int(input('Введите размер сигнатуры (16 по умолчанию): ') or 16)

path_to_original_file = input('Введите путь до исходного файла (original-file.txt по умолчанию): ') \
                        or 'folder-with-files/original-file.txt'

with open(path_to_original_file, 'rb') as path:
    file = mmap.mmap(path.fileno(), 0, access=mmap.ACCESS_READ)
    file.seek(offset)
    signature = file.read(signature_size)

path_to_directory = input('Введите путь до директории (folder-with-files по умолчанию): ') \
                        or 'folder-with-files'

os.chdir(path_to_directory)
path_to_files = []
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        path_to_files.append(os.path.join(root, name))

files_with_signatures = []
for file_path in path_to_files:
    with open(file_path, 'rb') as path:
        file = mmap.mmap(path.fileno(), 0, access=mmap.ACCESS_READ)
        file.seek(0)
        if file.find(signature) != -1:
            files_with_signatures.append(file_path)

print('Пути к файлам с заданной сигнатурой: ')
for x in files_with_signatures:
    print(x)
