# Фамилия,Имя,Отчество,Телефон

import os

# 1
def show():
    with open(FILE_PATH,'r',encoding='utf-8') as f:
        flagEnd = False
        while not flagEnd:
            info=f.readline()
            if info:
                print(info)
            else:
                flagEnd=True
# 2
def search():
    searchValue=input("Введите строку поиска:")
    with open(FILE_PATH,'r',encoding='utf-8') as f:
        flagEnd = False
        while not flagEnd:
            info=f.readline()
            if info:
                if searchValue in info:
                    print(info)
            else:
                flagEnd=True
# 3
def add():
    family=input("Введите фамилию: ")
    name=input("Введите имя: ")
    midname=input("Введите отчество: ")
    phone=input("Введите телефон: ")
    with open(FILE_PATH,'a',encoding='utf-8') as f:
            f.write(family+','+name+','+midname+','+phone+'\n')

# 4
def edit():
    index=int(input("Введите индекс: "))
    family=input("Введите фамилию: ")
    name=input("Введите имя: ")
    midname=input("Введите отчество: ")
    phone=input("Введите телефон: ")
    with open(FILE_PATH,'r',encoding='utf-8') as f1:
        with open(FILE_PATH_TEMP,'w',encoding='utf-8') as f2:
            flagEnd = False
            print(index)
            i=0
            while not flagEnd:
                info=f1.readline()
                print(i)
                if info:
                    if index!=i:
                        f2.write(info)
                    else:
                        f2.write(family+','+name+','+midname+','+phone+'\n')
                else:
                    flagEnd=True
                i += 1
    os.remove(FILE_PATH)  
    os.rename(FILE_PATH_TEMP,FILE_PATH)

# 5
def delete():
    index=int(input("Введите индекс: "))
    with open(FILE_PATH,'r',encoding='utf-8') as f1:
        with open(FILE_PATH_TEMP,'w',encoding='utf-8') as f2:
            flagEnd = False
            i=0
            while not flagEnd:
                info=f1.readline()
                if info:
                    if index!=i:
                        f2.write(info)
                else:
                    flagEnd=True
                i+=1
    os.remove(FILE_PATH)  
    os.rename(FILE_PATH_TEMP,FILE_PATH)

FILE_PATH = r"data\base.txt"
FILE_PATH_TEMP = r"data\base_temp.txt"

flagExit=False

while not flagExit:
    print('[1] Показать')
    print('[2] Поиск')
    print('[3] Добавить')
    print('[4] Редактировать')
    print('[5] Удалить')
    print('[6] Выход')
    print()
    res = int(input("Введите номер: "))

    if res ==1:
        show()
    elif res==2:
        search()
    elif res==3:
        add()
    elif res==4:
        edit()
    elif res==5:
        delete()
    elif res==6:
        flagExit=True


