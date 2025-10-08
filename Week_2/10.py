# Задание 10.  
# Написать программу для имитации игры в дартс. Играет два игрока.  
# Пользователь “кидает” три дротика, каждый раз случайно получая очки  
# от 1 до 20. Очки за каждый бросок с некоторой случайной вероятностью  
# могут быть удвоены/утроены. Вывести результат каждого “броска”, 
# сумму очков и победителя.
import random
drot1, drot2, drot3 = map(int,input().split())
drot11, drot22, drot33 = map(int,input().split())
drot1 =  drot1 *random.randint(1, 3)
print(drot1)
drot2 =  drot2* random.randint(1, 3)
print(drot2)
drot3 =  drot3* random.randint(1, 3)
print(drot3)
drot11 =  drot11* random.randint(1, 3)
print(drot11)
drot22 =  drot22* random.randint(1, 3)
print(drot22)
drot33 =  drot33* random.randint(1, 3)
print(drot33)
ochki = drot1 + drot2 + drot3 
ochkii = drot11 + drot22 + drot33 
if ochki > ochkii:
    print(ochki, ochkii, "Выиграл игрок 1")
else:
    print(ochki, ochkii, "Выиграл игрок 2")
