#Задание 4.
#Реализовать игру в виселицу. Программа выбирает слово из заранее 
#подготовленного списка и рисует на экране столько прочерков, сколько букв 
#в этом слове. Пользователь должен отгадать, какое слово загадано 
#программой. В каждый ход играющий указывает одну букву. Если названа 
#буква, входящая в состав слова, она подставляется вместо соответствующего 
#прочерка. В противном случае играющий теряет 1 очко. В начальный момент 
#у играющего 15 очков. Каждый ход выводить текущий результат угадывания, 
#количество оставшихся очков и уже названные неверные буквы.

import random

word_list = ["apple", "banana", "orange" ]
word = random.choice(word_list)
n = len(word)
procherk = n * "_"
procherk = list(procherk)

score = 15
wrong_lett = []
while score > 0 and word != "".join(procherk):
    letter = input()
    
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                procherk[i] = letter
    else:
        if letter not in wrong_lett:
            wrong_lett.append(letter)
            score -= 1
        
        print('Неправильные буквы:', wrong_lett)

    print("".join(procherk), '<-')
    print(score)


if score:
    print("Победа!!! очков: ", score)
else:
    print('Не победа :(')