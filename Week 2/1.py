import math
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
print(p)
S_tre = math.sqrt( (p * (p - a) * (p - b) * (p - c)))
R_tre = ((a*b*c)/(4*S_tre))
print(R_tre)
S_okr = math.pi * R_tre**2
print("Формула Герона", S_tre, "площадь описанной окружности", S_okr)
