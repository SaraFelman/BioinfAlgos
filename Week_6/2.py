# Задание 2.
# Напишите программу, которая при помощи регулярных выражений и
# библиотеки re делала бы следующее:
# 1) В первой строке меняла местами слово и следующее за ним число.
# 2) Находила все строки, которые начинаются на ‘М’ или ‘С’ и заканчиваются точкой.
# 3) Находила и записывала все ссылки в отдельный файл.
# 4) Находила все слова, содержащие английские и русские буквы (примеры: ‘email-адресов’, ‘реgулярным’).
# 5) Добавляла недостающий пробел между знаком препинания и словом.
# 6) Меняла букву на заглавную у первого слова в новом предложении.
# В качестве примера используйте файл text_for_regex_training.txt.

import re

with open("text_for_regex_training.txt", "r", encoding="UTF-8") as r_file:
    s = r_file.read()
    # print(s)

    # "Творчество Gemini 1.5 Flash 002"
    print(re.sub(r'(\w+)(\s)(\d.\d)', r'\3\2\1', "Творчество Gemini 1.5 Flash 002"))

    match2 = re.findall(r'^[МMCС].*\.$', s, re.MULTILINE) # 2)
    print(match2[0] if match2 else "Не найден")

    match3 = re.findall(r'https://[\w.\\@/-]+', s)  # 3)3
    if match3:
        with open(f'./emails.txt', 'w') as out_file:
            out_file.write('\n'.join(match3))
            print("\n3) Ссылки сохранены в ./emails.txt")
    else:
        print("\n3) Ссылки не найдены")
    # (https://

    match4 = re.findall(r'\b(?=[A-Za-zА-Яа-я-]*[A-Za-z])(?=[A-Za-zА-Яа-я-]*[А-Яа-я])[A-Za-zА-Яа-я-]+\b', s)
    print(match4[0] if match4 else "хз") # 4)

    # 5) Добавляла недостающий пробел между знаком препинания и словом.
    s = re.sub(r'([.,;!?])([^\s])', r'\1 \2', s) # 5)
    # print(s)

    # 6) Меняла букву на заглавную у первого слова в новом предложении.
    s = re.sub(r'(^|[.!?]\s+)([а-яa-z])', lambda m: m.group(1) + m.group(2).upper(), s)

with open("text_for_regex_training_fixed.txt", "w", encoding="utf-8") as out:
    out.write(s)



