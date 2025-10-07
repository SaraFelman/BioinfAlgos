import csv

with open("C:\Users\molge\OneDrive\Documents\GitHub\BioinfAlgos\Week_5\BindingEnergy1.txt", "r", encoding="UTF-8") as r_file:
    # "C:\Users\molge\OneDrive\Документы\GitHub\BioinfAlgos\Week_5\BindingEnergy1.txt"
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = []
    max1 = 0
    max2 = 0
    max3 = 0
    max4 = 0
    max5 = 0
    max_string1 = []
    max_string2 = []
    max_string3 = []
    max_string4 = []
    max_string5 = []
    # Считывание данных из CSV файла
    for row in file_reader:
        sum_kvad_otkl = (row["m1"] - row["control"])**2 + (row["m2"] - row["control"])**2 + (row["m3"] - row["control"])**2 + (row["m4"] - row["control"])**2 + (row["m5"] - row["control"])**2 + (row["m6"] - row["control"])**2
        if sum_kvad_otkl >= max1:
            max1 = sum_kvad_otkl 
            max_string1 = row[i]
        print(max_string1)
        # if sum_kvad_otkl <  max1:
        #     if sum_kvad_otkl > max2:
        #     max_string2 = row[i]

    #         # Вывод строки, содержащей заголовки для столбцов
    #         print(f'Файл содержит столбцы: {", ".join(row)}')
    #     else:
    #         # Вывод строк
    #         print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
    #     count += 1
    # print(f'Всего в файле {count} строк.')