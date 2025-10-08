#Задание 1.
#Напишите программу, которая бы определяла изограммы – строки 
#без повторяющихся букв.

my_str = input()
isogramm = True

for i in range(len(my_str) - 1):
    for j in range(i + 1, len(my_str) - 1):
        if my_str[i] == my_str[j]:
            isogramm = False
            break

if isogramm: 
    print("Изограмма") 
else:
    print("Не изограмма")