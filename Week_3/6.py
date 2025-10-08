# Задание 6. 
# Напишите программу, которая  найдёт в последовательности ДНК  все старт 
# кодоны и выведет на экран список индексов их начал. 
# Входные данные: dna_sequence = 'ATGACGTCGAAATGCGTAATGCTAGGACCCCTAGATG' 
# Результат: [0, 11, 18, 34]

dna_sequence = 'ATGACGTCGAAATGCGTAATGCTAGGACCCCTAGATG'
a = dna_sequence.find('ATG')
my_str = []
while a != -1: # то есть старт кодон есть в послед 
    my_str.append(a) 
    a = dna_sequence.find('ATG', a+1) #строка и с какого символа будем искать
print(my_str)
