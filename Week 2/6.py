#6
#Есть 2 колонии бактерии, клетки в которых делятся с разной скоростью. 
#В 1 колонии клетки делятся в среднем 3 раза в час, а во 2 колонии клетки делятся 2 раза в час. 
#Посчитайте сколько всего будет бактерий через 10 часов, если известна начальная численность колоний.
#Входные данные: first_colony = 3 second_colony = 6
#Результат: 3227516928

first_colony = int(input())
second_colony = int(input())
time = 10
for i in range(time):
    first_colony = first_colony * 8
    second_colony = second_colony * 4 
print(first_colony + second_colony)
