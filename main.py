from operator import index
import sys
UserCar=[]
Cars=[]
with open('UserCar.txt','r',encoding='utf=8') as f:
    with open('kolcars.txt','r') as file:
        I=file.readlines()
        I=I[0]
        I=int(I)
        for a in range(0, I):
            for b in range(0,5):
                y = f.readline()
                y = y.rstrip('\n')
                UserCar.append(y)
                if UserCar[0] == '':
                    UserCar = []
    with open('UserCar.txt','w',encoding='utf=8') as f:
        pass
with open('cars.txt','r') as f:
    v=len(UserCar)
    v=v//5
    for a in range(0,v+1):
        y=f.readline()
        y=y.rstrip('\n')
        Cars.append(y)
    Cars.pop(-1)
# N=1
# if N !=1:
#       UserCar = ['Ferrari California', 'Ferrari', 'красный', 'V8 - автоматическая', 'светодиодные (LED)']
#       Cars=['Ferrari California']
if Cars==[]:
    Cars=[]
car = 0
company = 1
colour = 2
box = 3
headlights = 4
x = 0
f = 0
while x!=1:
    Biblioteka = [UserCar]
    print(UserCar)
    print('если вы хотите увидеть таблицу, ввидите tab')
    print('если вы хотите узнать х-ки машины, введите её нaзвание')
    print(Cars)
    print('если вы хотите добавить свою напишите add')
    print('если вы хотите удалить данные машины, напишите: del')
    print('что бы выйти напишите end')
    print(UserCar)
    print(I)
    print(Cars)
    name=input()
    # завершение программы и сохранение
    if name =='end':
        s=len(Cars)
        with open('kolcars.txt','w') as f:
            f.write(str(s))
        g=len(UserCar)
        print(g)
        if g==0:
            print('завершение программы....')
            break
        print('завершение программы....')
        for n in range(0,g):
            l = UserCar[n]
            with open('UserCar.txt', 'a', encoding='utf-8') as file:
                file.write(l + '\n')
        with open('cars.txt', 'w', encoding='utf-8') as file:
            for Cars in Cars:
                file.write(Cars + '\n')
        break
    if name =='tab':
            print('|компания      |производитель      |цвет мащины      |тип коробки передач |фары машины          |')
            print('—————————————————————————————————————————————————————————————————————————————————————————————————')
            for i in range (0,I):
                comp=len(UserCar[i*5])
                comp=14-comp
                prois=len(UserCar[i*5+1])
                prois=19-prois
                colores=len(UserCar[i*5+2])
                colores=17-colores
                peredacha=len(UserCar[i*5+3])
                peredacha=20-peredacha
                fara=len(UserCar[i*5+4])
                fara=21-fara
                print('|'+UserCar[i*5]+' '*comp+'|'+UserCar[i*5+1]+' '*prois+'|'+UserCar[i*5+2]+' '* colores+'|'+UserCar[i*5+3]+' '*peredacha+'|'+UserCar[i*5+4]+' '*fara+'|')
                print('—————————————————————————————————————————————————————————————————————————————————————————————————')
                continue
    # удаляем машину
    elif name == 'del':
        print('напишите название машины из списка:')
        print(Cars)
        deleting = input()
        if deleting not in Cars:
            print('===============================')
            print('данные неверны')
            print('===============================')
            continue
        else:
            m=Cars.index(deleting)
            UserCar.pop(m*5)
            UserCar.pop(m*5)
            UserCar.pop(m*5)
            UserCar.pop(m*5)
            UserCar.pop(m*5)
            Cars.pop(m)
            I=I-1
    # Добавляем информацию
    elif name=='add':
            print('введите название машины:')
            s = input()
            Cars.append(s)
            UserCar.append(s)
            print('введите компанию производителя машины:')
            s = input()
            UserCar.append(s)
            print('введите цвет машины:')
            s = input()
            UserCar.append(s)
            print('введите тип коробки передач машины:')
            s = input()
            UserCar.append(s)
            print('введите фары машины:')
            s = input()
            UserCar.append(s)
            I=I+1
            continue
    # проверка на лоха
    if name=='del' or name=='add':
        continue
    if not (name in Cars):
        print('==============================')
        print('данные неверны')
        print('==============================')
        continue
    a = Cars.index(name)
    # информация о тачках
    print("============================================================================================")
    print('название:', UserCar[a * 5])
    print('компания:', UserCar[a * 5 + 1])
    print('цвет:', UserCar[a * 5 + 2])
    print('тип передач:', UserCar[a * 5 + 3])
    print('фары:', UserCar[a * 5 + 4])
    print("============================================================================================")
    print('введите что угодно, чтобы вернуться в меню.')
    h = input()
