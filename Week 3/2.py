#Задание 2.
#В переменной sequence находится последовательность белка или РНК. 
#Информация о том, какая именно там последовательность содержится в 
#переменных protein и RNA: если последовательность белковая, то в protein 
#будет True, а если РНКовая, то True будет в RNA. Если последовательность 
#белковая, то нужно посчитать, сколько понадобилось тРНК для её синтеза. А 
#если в последовательности находится РНК, то нужно посчитать сколько 
#потребуется тРНК для её перевода в белок. 
#Входные данные: 
#sequence = 'RSNTKRPLGPKYIFAEHGDAE'; protein = True ; RNA = False 
#Результат: 21 
#Входные данные: 
#sequence = 'AGCUAGCUAGCUAGCUAGCUAGCUAGCUAGC' 
#protein = False ; RNA = True 
#Результат: 10

sequence = input()
sequence_list = list(sequence)
protein = True
RNA = False

for i in sequence_list:
    if i != "U":
        continue
    else:
        protein = False
        RNA = True
        print("protein = False; RNA = True")
        break

if protein == True and RNA == False:
    print("protein = True; RNA = False")
    res_protein = len(sequence)
    print(res_protein)
else:
    res_RNA = len(sequence)// 3
    print(res_RNA)
