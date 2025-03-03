import os

# Создание каталога
# os.mkdir("folder")


# Проверка существ пути
if os.path.exists("folder"):
    # запись в каталог
    with open("folder/file.txt", 'w') as file:
        pass

if os.path.isfile("folder"):
    print('file')
else:
    print('no file')


dogs_imager = []
print(os.listdir("folder"))

