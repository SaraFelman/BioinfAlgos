import csv
(x_i – μ)²

with open(" BindingEnergy.txt", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    sum_kvad_otkl = []
    
    srednee = 
    n = 6
    # Считывание данных из CSV файла
    for row in file_reader:
        kvad_otkl = ( ( (nabludenie - srednee)**2) / n) ** 0.5
        if kvad_otkl > count:
            count = kvad_otkl

            # Вывод строки, содержащей заголовки для столбцов
            print(f'Файл содержит столбцы: {", ".join(row)}')
        else:
            # Вывод строк
            print(f'    {row[0]} - {row[1]} и он родился в {row[2]} году.')
        count += 1
    print(f'Всего в файле {count} строк.')