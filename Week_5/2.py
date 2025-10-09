import os

def reading(file_name):
    assert os.path.exists(file_name), f"Файл {file_name} не найден!"
    features = []
    cds = []

    with open(file_name, "r", encoding="UTF-8") as r_file:
        # r_file = r_file.read()
        flag = False
        for row in r_file:
            if row.startswith("FEATURES"):
                flag = True
                continue
            if row.startswith("ORIGIN"):
                flag = False
                break
            if flag:
                features.append(row)
                if "CDS" in row or "/translation" in row:
                    cds.append(row)
    return features, cds
 

def writing(features, cds):
    # assert os.path.exists(file_name), f"Файл {file_name} не найден!"
    with open("./parsing_genbank/features.txt", "w", encoding="utf-8") as f1:
        f1.writelines(features)
    with open("./parsing_genbank/cds.txt", "w", encoding="utf-8") as f2:
        f2.writelines(cds)
    # return features, cds

file_name = input("Введите имя файла: ")
feat1 = input("Введите куда записать feature: ")
cd1 = input("Введите куда записать cds: ")
# /Users/fixed/PycharmProjects/BioinfAlgos/Week_5/parsing_genbank/sequence.gb

features, cds = reading(file_name)
writing(features, cds)
print(features)
print(cds)
# print(open("./parsing_genbank/features.txt", encoding="utf-8").read())
# print(open("./parsing_genbank/cds.txt", encoding="utf-8").read())
features_path = "./parsing_genbank/features.txt"
cds_path = "./parsing_genbank/cds.txt"

# with open(features_path, "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     print("".join(lines[:15]))
#
# with open(cds_path, "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     print("".join(lines[:15]))