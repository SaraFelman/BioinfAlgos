import csv
(x_i – μ)²

with open(" BindingEnergy.txt", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = []
   
    # Считывание данных из CSV файла
    for row in file_reader:
        sum_kvad_otkl = (row["m1"] - row["control"])**2 + (row["m2"] - row["control"])**2 + (row["m3"] - row["control"])**2 + (row["m4"] - row["control"])**2 + (row["m5"] - row["control"])**2 + (row["m6"] - row["control"])**2
        

            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
        count += 1
    print(f'Всего в файле {count} строк.')