#5
a = int(input())
my_list = []
while a > 0:
    my_list.append(a % 2)
    a = a //2
for i in range(len(my_list) - 1, -1, -1):
    print(my_list[i], end="")

#print(*my_list[::-1], sep="")
