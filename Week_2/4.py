#a,b = map(input().split())
a = int(input())
a_12 = a//10
a3 = a - (a//10 *10) # = 3
a1 = a_12 //10  # = 1
a2 = a//10 - 10 # = 2
schetchik = 0
if a1//2 == a1/2:
    schetchik = +1
if a2//2 == a2/2:
    schetchik = +1
if a3//2 == a3/2:
    schetchik = +1
print(a, a_12, a1, a2, a3)
print(schetchik)
