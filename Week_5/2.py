import os
from imaplib import Continuation


def reading(file_name):
    assert os.path.exists(file_name), f"Файл {file_name} не найден!"
    features = []
    cds = []

    with open(file_name, "r", encoding="UTF-8") as r_file:
        # r_file = r_file.read()
        flag_features = False
        flag_cds = False

        flag_features = False
        flag_cds = False

        for row in r_file:
            if row.startswith("FEATURES"):
                flag_features = True
                continue

            if row.startswith("ORIGIN"):
                flag_features = False
                flag_cds = False
                break

            if row.strip().startswith("CDS"):
                flag_cds = True
                cds.append(row)
                continue

            if flag_cds:
                if row[:5].strip() != "" and not row.startswith("                     /"):
                    flag_cds = False
                else:
                    cds.append(row)

            if flag_features:
                features.append(row)
    return features, cds
 

def writing(features, cds):
    # assert os.path.exists(file_name), f"Файл {file_name} не найден!"
    with open("./parsing_genbank/features.txt", "w", encoding="utf-8") as f1:
        f1.writelines(features)
    with open("./parsing_genbank/cds.txt", "w", encoding="utf-8") as f2:
        f2.writelines(cds)
    # return features, cds

# /Users/fixed/PycharmProjects/BioinfAlgos/Week_5/parsing_genbank/sequence.gb
file_name = input("Введите имя файла: ")
features, cds = reading(file_name)
writing(features, cds)
print(features)
print(cds)

# print(open("./parsing_genbank/features.txt", encoding="utf-8").read())
# print(open("./parsing_genbank/cds.txt", encoding="utf-8").read())

# with open(features_path, "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     print("".join(lines[:15]))
#
# with open(cds_path, "r", encoding="utf-8") as f:
#     lines = f.readlines()
#     print("".join(lines[:15]))