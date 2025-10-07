
with open("BindingEnergy1.txt", "r", encoding="UTF-8") as r_file:
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
    for row in r_file:
        string = row.split(sep=None, maxsplit=-1)
        sum_kvad_otkl = round(((float(string[1]) - float(string[0]))**2)  + ((float(string[2]) - float(string[0]))**2) + ((float(string[3]) - float(string[0]))**2) + ((float(string[4]) - float(string[0]))**2)+ ((float(string[5]) - float(string[0]))**2)+ ((float(string[6]) - float(string[0]))**2))
        count.append(sum_kvad_otkl)
        if sum_kvad_otkl >= max1:
            max1 = sum_kvad_otkl 
            max_string1.append(string)
        else:
            if sum_kvad_otkl >= max2:
                max2 = sum_kvad_otkl 
                max_string2.append(string)
            else:
                if sum_kvad_otkl >= max3:
                    max3 = sum_kvad_otkl 
                    max_string3.append(string)
                else:
                    if sum_kvad_otkl >= max4:
                        max4 = sum_kvad_otkl 
                        max_string4.append(string)
                    else:
                        if sum_kvad_otkl >= max5:
                            max5 = sum_kvad_otkl 
                            max_string5.append(string)
print(count)                                            
print(max1, max2, max3, max4, max5)
# print(max_string1)
# print(max_string2)
# print(max_string3)
# print(max_string4)
# print(max_string5)
    
       
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