# Задание 3.
# Создайте программу, которая проводит транскрипцию ДНК с шести
# возможных рамок считывания. Далее программа выбирает самый длинный 
# вариант РНК, транслирует его, выводит соответствующие последовательности
# РНК и белка, а так же их длины. Для трансляции используйте словарь:

rna_codon_table = { 
 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 
 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', 
 'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 
'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 
'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 
'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 
'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 
'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 
'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 
'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 
'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G' }

dna_matr = "agcaccacggcagcaggaggtttcggctaagttggaggtactggccacgactgcatgcccgcgcccgccaggtgatacctccgccggtgacccaggggctctgcgacacaaggagtctgcatgtctaagtgctagacatgctcagctttgtggatacgcggactttgttgctgcttgcagtaaccttatgcctagcaacatgccaatctttacaagaggaaactgtaagaaagggcccagccggagatagaggaccacgtggagaaaggggtccaccaggccccccaggcagagatggtgaagatggtcccacaggccctcctggtccacctggtcctcctggcccccctggtctcggtgggaactttgctgctcagtatgatggaaaaggagttggacttggccctggaccaatgggcttaatgggacctagaggcccacctggtgcagctggagccccaggccctcaaggtttccaaggacctgctggtgagcctggtgaacctggtcaaactggtcctgcaggtgctcgtggtccagctggccctcctggcaaggctggtgaagatggtcaccctggaaaacccggacgacctggtgagagaggagttgttggaccacagggtgctcgtggtttccctggaactcctggacttcctggcttcaaaggcattaggggacacaatggtctggatggattgaagggacagcccggtgctcctggtgtgaagggtgaacctggtgcccctggtgaaaatggaactccaggtcaaacaggagcccgtgggcttcctggtgagagaggacgtgttggtgcccctggcccagctggtgcccgtggcagtgatggaagtgtgggtcccgtgggtcctgctggtcccattgggtctgctggccctccaggcttcccaggtgcccctggccccaagggtgaaattggagctgttggtaacgctggtcctgctggtcccgccggtccccgtggtgaagtgggtcttccaggcctctccggccccgttggacctcctggtaatcctggagcaaacggccttactggtgccaagggtgctgctggccttcccggcgttgctggggctcccggcctccctggaccccgcggtattcctggccctgttggtgctgccggtgctactggtgccagaggacttgttggtgagcctggtccagctggctccaaaggagagagcggtaacaagggtgagcccggctctgctgggccccaaggtcctcctggtcccagtggtgaagaaggaaagagaggccctaatggggaagctggatctgccggccctccaggacctcctgggctgagaggtagtcctggttctcgtggtcttcctggagctgatggcagagctggcgtcatgggccctcctggtagtcgtggtgcaagtggccctgctggagtccgaggacctaatggagatgctggtcgccctggggagcctggtctcatgggacccagaggtcttcctggttcccctggaaatatcggccccgctggaaaagaaggtcctgtcggcctccctggcatcgacggcaggcctggcccaattggcccagctggagcaagaggagagcctggcaacattggattccctggacccaaaggccccactggtgatcctggcaaaaacggtgataaaggtcatgctggtcttgctggtgctcggggtgctccaggtcctgatggaaacaatggtgctcagggacctcctggaccacagggtgttcaaggtggaaaaggtgaacagggtccccctggtcctccaggcttccagggtctgcctggcccctcaggtcccgctggtgaagttggcaaaccaggagaaaggggtctccatggtgagtttggtctccctggtcctgctggtccaagaggggaacgcggtcccccaggtgagagtggtgctgccggtcctactggtcctattggaagccgaggtccttctggacccccagggcctgatggaaacaagggtgaacctggtgtggttggtgctgtgggcactgctggtccatctggtcctagtggactcccaggagagaggggtgctgctggcatacctggaggcaagggagaaaagggtgaacctggtctcagaggtgaaattggtaaccctggcagagatggtgctcgtggtgctcctggtgctgtaggtgcccctggtcctgctggagccacaggtgaccggggcgaagctggggctgctggtcctgctggtcctgctggtcctcggggaagccctggtgaacgtggtgaggtcggtcctgctggccccaatggatttgctggtcctgctggtgctgctggtcaacctggtgctaaaggagaaagaggagccaaagggcctaagggtgaaaacggtgttgttggtcccacaggccccgttggagctgctggcccagctggtccaaatggtccccccggtcctgctggaagtcgtggtgatggaggcccccctggtatgactggtttccctggtgctgctggacggactggtcccccaggaccctctggtatttctggccctcctggtccccctggtcctgctgggaaagaagggcttcgtggtcctcgtggtgaccaaggtccagttggccgaactggagaagtaggtgcagttggtccccctggcttcgctggtgagaagggtccctctggagaggctggtactgctggacctcctggcactccaggtcctcagggtcttcttggtgctcctggtattctgggtctccctggctcgagaggtgaacgtggtctaccaggtgttgctggtgctgtgggtgaacctggtcctcttggcattgccggccctcctggggcccgtggtcctcctggtgctgtgggtagtcctggagtcaacggtgctcctggtgaagctggtcgtgatggcaaccctgggaacgatggtcccccaggtcgcgatggtcaacccggacacaagggagagcgcggttaccctggcaatattggtcccgttggtgctgcaggtgcacctggtcctcatggccccgtgggtcctgctggcaaacatggaaaccgtggtgaaactggtccttctggtcctgttggtcctgctggtgctgttggcccaagaggtcctagtggcccacaaggcattcgtggcgataagggagagcccggtgaaaaggggcccagaggtcttcctggcttaaagggacacaatggattgcaaggtctgcctggtatcgctggtcaccatggtgatcaaggtgctcctggctccgtgggtcctgctggtcctaggggccctgctggtccttctggccctgctggaaaagatggtcgcactggacatcctggtacagttggacctgctggcattcgaggccctcagggtcaccaaggccctgctggcccccctggtccccctggccctcctggacctccaggtgtaagcggtggtggttatgactttggttacgatggagacttctacagggctgaccagcctcgctcagcaccttctctcagacccaaggactatgaagttgatgctactctgaagtctctcaacaaccagattgagacccttcttactcctgaaggctctagaaagaacccagctcgcacatgccgtgacttgagactcagccacccagagtggagcagtggttactactggattgaccctaaccaaggatgcactatggatgctatcaaagtatactgtgatttctctactggcgaaacctgtatccgggcccaacctgaaaacatcccagccaagaactggtataggagctccaaggacaagaaacacgtctggctaggagaaactatcaatgctggcagccagtttgaatataatgtagaaggagtgacttccaaggaaatggctacccaacttgccttcatgcgcctgctggccaactatgcctctcagaacatcacctaccactgcaagaacagcattgcatacatggatgaggagactggcaacctgaaaaaggctgtcattctacagggctctaatgatgttgaacttgttgctgagggcaacagcaggttcacttacactgttcttgtagatggctgctctaaaaagacaaatgaatggggaaagacaatcattgaatacaaaacaaataagccatcacgcctgcccttccttgatattgcacctttggacatcggtggtgctgaccaggaattctttgtggacattggcccagtctgtttcaaataaatgaactcaatctaaattaaaaaagaaagaaatttgaaaaaactttctctttgccatttcttcttcttcttttttaactgaaagctgaatccttccatttcttctgcacatctacttgcttaaattgtgggcaaaagagaaaaagaaggattgatcagagcattgtgcaatacagtttcattaactccttcccccgctcccccaaaaatttgaatttttttttcaacactcttacacctgttatggaaaatgtcaacctttgtaagaaaaccaaaataaaaattgaaaaataaaaaccataaacatttgcaccacttgtggcttttgaatatcttccacagagggaagtttaaaacccaaacttccaaaggtttaaactacctcaaaacactttcccatgagtgtgatccacattgttaggtgctgacctagacagagatgaactgaggtccttgttttgttttgttcataatacaaaggtgctaattaatagtatttcagatacttgaagaatgttgatggtgctagaagaatttgagaagaaatactcctgtattgagttgtatcgtgtggtgtattttttaaaaaatttgatttagcattcatattttccatcttattcccaattaaaagtatgcagattatttgcccaaatcttcttcagattcagcatttgttctttgccagtctcattttcatcttcttccatggttccacagaagctttgtttcttgggcaagcagaaaaattaaattgtacctattttgtatatgtgagatgtttaaataaattgtgaaaaaaatgaaataaagcatgtttggttttccaaaagaa" 
dna_matr = dna_matr.upper()

# ищем ДНК обратную
dna_reverse = []
for i in dna_matr:
    if i == 'A':
        dna_reverse.append('T')
    if i == 'T':
        dna_reverse.append('A')
    if i == 'G':
        dna_reverse.append('C')
    if i == 'C':
        dna_reverse.append('G')
dna_reverse = "".join(dna_reverse)
#print("dna_reverse", dna_reverse)

# разбиваем обе ДНК на триплеты (6 рамок считывания) и кладем в список 
dna_matr_tripl_1 = []
dna_matr_tripl_2 = []
dna_matr_tripl_3 = []

for i in range(0, len(dna_matr), 3):
    tripl_1 = dna_matr[i: i+3]
    if len(tripl_1) == 3:
        dna_matr_tripl_1.append(tripl_1)


for i in range(1, len(dna_matr), 3):
    tripl_2 = dna_matr[i: i+3]
    if len(tripl_2) == 3:
        dna_matr_tripl_2.append(tripl_2)
        
for i in range(2, len(dna_matr), 3):
    tripl_3 = dna_matr[i: i+3]
    if len(tripl_3) == 3:
        dna_matr_tripl_3.append(tripl_3)        
#print("dna_matr_tripl_1", dna_matr_tripl_1)         

dna_reverse_tripl_1 = []
dna_reverse_tripl_2 = []
dna_reverse_tripl_3 = []

for i in range(0, len(dna_reverse), 3):
    tripll_1 = dna_reverse[i: i+3]
    if len(tripll_1) == 3:
        dna_reverse_tripl_1.append(tripll_1)
        
for i in range(1, len(dna_reverse), 3):
    tripll_2 = dna_reverse[i: i+3]
    if len(tripll_2) == 3:
        dna_reverse_tripl_2.append(tripll_2)        

for i in range(2, len(dna_reverse), 3):
    tripll_3 = dna_reverse[i: i+3]
    if len(tripll_3) == 3:
        dna_reverse_tripl_3.append(tripll_3)        
#print("dna_reverse_tripl_1", dna_reverse_tripl_1)   

rm_1 = ''.join(dna_matr_tripl_1)
rm_2 = ''.join(dna_matr_tripl_2)
rm_3 = ''.join(dna_matr_tripl_3)

rr_1 = ''.join(dna_reverse_tripl_1)
rr_2 = ''.join(dna_reverse_tripl_2)
rr_3 = ''.join(dna_reverse_tripl_3)

# ищем РНК, пока в формате строки 
rna_matr_1 = rm_1.replace('T','U')
rna_matr_2 = rm_2.replace('T','U')
rna_matr_3 = rm_3.replace('T','U')

rna_reverse_1 = rr_1.replace('T','U')
rna_reverse_2 = rr_2.replace('T','U')
rna_reverse_3 = rr_3.replace('T','U')
# print("rna_reverse_1", rna_reverse_1)
# print("rna_reverse_2", rna_reverse_2)

# делаем РНК триплетами
tripl_1 = 0 
tripl_2 = 0 
tripl_3 = 0

len_rna = {}
max_key = 0 
max_val = 0

rna_matr_tripl_1 = []
rna_matr_tripl_2 = []
rna_matr_tripl_3 = []

for i in range(0, len(rna_matr_1), 3):
    tripl_1 = rna_matr_1[i: i+3]
    if len(tripl_1) == 3:
        rna_matr_tripl_1.append(tripl_1)
for i in range(0, len(rna_matr_2), 3):
    tripl_2 = rna_matr_2[i: i+3]
    if len(tripl_2) == 3:
        rna_matr_tripl_2.append(tripl_2)
for i in range(0, len(rna_matr_3), 3):
    tripl_3 = rna_matr_3[i: i+3]
    if len(tripl_3) == 3:
        rna_matr_tripl_3.append(tripl_3)        
# print("rna_matr_tripl_1 ", rna_matr_tripl_1 )
# print("rna_matr_tripl_2 ", rna_matr_tripl_2 )         

rna_reverse_tripl_1 = []
rna_reverse_tripl_2 = []
rna_reverse_tripl_3 = []

for i in range(0, len(rna_reverse_1), 3):
    tripl_1 = rna_reverse_1[i: i+3]
    if len(tripl_1) == 3:
        rna_reverse_tripl_1.append(tripl_1)
for i in range(0, len(rna_reverse_2), 3):
    tripl_2 = rna_reverse_2[i: i+3]
    if len(tripl_2) == 3:
        rna_reverse_tripl_2.append(tripl_2)
for i in range(0, len(rna_reverse_3), 3):
    tripl_3 = rna_reverse_3[i: i+3]
    if len(tripl_3) == 3:
        rna_reverse_tripl_3.append(tripl_3) 

#print("rna_reverse_tripl_1 ", rna_reverse_tripl_1 )


protein_curr_1 = []
protein_curr_2 = []
protein_curr_3 = []

protein_curr_11 = []
protein_curr_22 = []
protein_curr_33 = []


for triplet in rna_matr_tripl_1:
    if triplet in rna_codon_table and rna_codon_table[triplet] != '*':
        protein_curr_1.append(rna_codon_table[triplet])
    if rna_codon_table[triplet] == '*':
        break
# print("protein_curr_1", protein_curr_1)

 
for triplet in rna_matr_tripl_2:
    if triplet in rna_codon_table and rna_codon_table[triplet] != '*':
        protein_curr_2.append(rna_codon_table[triplet])
    if rna_codon_table[triplet] == '*':
        break
# print("protein_curr_2", protein_curr_2)


for triplet in rna_matr_tripl_3:
    if triplet in rna_codon_table and rna_codon_table[triplet] != '*':
        protein_curr_3.append(rna_codon_table[triplet])
    if rna_codon_table[triplet] == '*':
        break

# белок для реверса 
for triplet in rna_reverse_tripl_1:
    if triplet in rna_codon_table and rna_codon_table[triplet] != '*':
        protein_curr_11.append(rna_codon_table[triplet])
    if rna_codon_table[triplet] == '*':
        break
# print("protein_curr_11", protein_curr_11)


for triplet in rna_reverse_tripl_2:
    if triplet in rna_codon_table and rna_codon_table[triplet] != '*':
        protein_curr_22.append(rna_codon_table[triplet])
    if rna_codon_table[triplet] == '*':
        break
# print("protein_curr_22", protein_curr_22) 


for triplet in rna_reverse_tripl_3:
    if triplet in rna_codon_table and rna_codon_table[triplet] != '*':
        protein_curr_33.append(rna_codon_table[triplet])
    if rna_codon_table[triplet] == '*':
        break
        

protein_all = {"protein_curr_1": len(protein_curr_1), "protein_curr_2": len(protein_curr_2), "protein_curr_3":len(protein_curr_3), "protein_curr_11":len(protein_curr_11), "protein_curr_22": len(protein_curr_22), "protein_curr_33":len(protein_curr_33)}
protein_all_2 = {"protein_curr_1": protein_curr_1, "protein_curr_2": protein_curr_2, "protein_curr_3": protein_curr_3, "protein_curr_11":protein_curr_11, "protein_curr_22": protein_curr_22, "protein_curr_33":protein_curr_33}
protein_rna = {"protein_curr_1": rna_matr_1, "protein_curr_2": rna_matr_2, "protein_curr_3": rna_matr_3, "protein_curr_11":rna_reverse_1, "protein_curr_22": rna_reverse_2, "protein_curr_33":rna_reverse_3}
#print("protein_all", protein_all)


max_value = 0
for key, value in protein_all.items(): 
    if value > max_value: 
        max_value = value 

keys = list(protein_all.keys())
index = list(protein_all.values()).index(max_value)
key = keys[index]

if key in protein_all_2:
    print("Белок максимального размера", "".join(protein_all_2[key]),", его размер", max_value, "аминокислот")
if key in protein_rna:
    print("РНК белка максимального размера", "".join(protein_rna[key]))
