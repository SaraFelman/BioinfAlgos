

def reading(file_name):
    with open(file_name, "r", encoding="UTF-8") as r_file:
        # r_file = r_file.read()
        features = []
        cds = []
        for row in r_file:
            if row.startswith("FEATURES"):
                while row.startswith("ORIGIN"):
                    features.append(row)   
        for row in r_file:
            if row.startswith("CDS"):
                while row.startswith("ORIGIN"):
                    cds.append(row)
    return features, cds                   
 

def writing(file_name):
    features = []
    cds = []
    for row in r_file:  
        with open(file_name, "w") as f:
            f.write(''.join(features))
    for row in r_file:
        with open(file_name, "w") as f:
            f.write(''.join(cds))
    return features, cds 

file_name = input("Введите имя файла: ") #"sequence.gb"               
# /BioinfAlgos/parsing_genbank/sequence.gb
reading(file_name)
writing(file_name)

print(features)
print(cds)