import re

# def car_numbers(match):
# kirilitca = [ "А", "В" , "Е", "К", "М", "Н", "О", "Р", "С", "Т", "У", "Х"]
# match = re.search(r'\w{1}\d{3}\w{2}\d{2}', "СС227Н69, С227НА69, Н087КТ799, АО36578, АН733147, 3733ММ45, ММ55АА23")
#
# print (match[0] if match else "Не найден")


pattern1 = r'\w{1}\d{3}\w{2}\d{2}'      #С227НА69
pattern2 = r'\w{2}\d{2}\\w{2}\d{3}'    #Н087КТ799
pattern3 = r'\w{1}\d{6}'                #АО36578
pattern4 = r'\w{2}\d{6}'                #АН733147
pattern5 = r'\d{4}\w{2}\d{2}'           #3733ММ45
pattern6 = r'\w{2}\d{2}\w{2}\d{2}'     #ММ55АА23
pattern = [pattern1, pattern2, pattern3, pattern4, pattern5, pattern6]

string = "СС227Н69, С227НА69, Н087КТ799, АО36578, АН733147, 3733ММ45, ММ55АА23"
for i in range(len(pattern)):
    match = re.search(pattern, string)
    print(match.groups())



    # match = re.search(r'\w{1}\d{3}\w{2}\d{2}'
    # match = re.search(r'\w{1}\d{3}\w{2}\d{2}'
    # match = re.search(r'\w{1}\d{3}\w{2}\d{2}'
    # match = re.search(r'\w{1}\d{3}\w{2}\d{2}'
    # match = re.search(r'\w{1}\d{3}\w{2}\d{2}'

# print(f"pattern{i}")
# С227НА69, Н087КТ799, АО36578, АН733147, 3733ММ45, ММ55АА23