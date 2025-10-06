# Задание 2. 
# Напишите программу, которая бы выводила содержимое предварительно 
# созданного словаря с идентификаторами (ключами) пяти генов. При вводе 
# идентификатора выведите название белка, который он кодирует. Сделать 
# возможность добавления ключа и значения в словарь, вводя их с клавиатуры 
# как пару «ключ-значение». 

# пример: NOS3 NITRIC_OXIDE_SYNTHASE_3
# a, b = ['key', 'value']

my_dict = {
    'APOA2': 'APOLIPOPROTEIN A-II', 'SLC4A1': 'ACANTHOCYTOSIS', 'CYP1A2': 'CYTOCHROME P450', 
    'ADRB2': 'BETA-2-ADRENERGIC RECEPTOR', 'ACE': 'ANGIOTENSIN I-CONVERTING ENZYME'
}

a = input("Напишите ключ значение через пробел") # инпут это для одной строки а если сплит то положит ки и айтем в разыне переменные 
if a:
    key, item = a.split() 
    if key not in my_dict:
        my_dict[key] = item
        print(my_dict)

vivod = input("Введите идентифекатор:") 
if vivod in my_dict:
    print(vivod, my_dict[vivod])    


#допилить проверку на то что ключ уже существует в словаре - done!
