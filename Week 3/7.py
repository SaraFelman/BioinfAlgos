# Задание 7. 
# Дан список с названиями генов. 
# Нужно: 1) Сделать новый список без повторяющихся генов 
# 2) Cделать отдельный список с генами, встречающимися более 3 раз 
# 3) Сделать возможности  пользователю добавить  новый элемент в список 
# или удалить элемент (с учетом проверки на уникальность). 
# Входные данные: genes = ['BRCA1', 'TP53', 'EGFR', 'BRCA2', 'BRCA1', 'EGFR', 'KRAS', 'BRCA1', 'TP53', 'BRCA1', 'KRAS', 'EGFR', 'PIK3CA', 'BRCA1', 'TP53', 'BRAF', 'EGFR', 'BRCA2', 'BRCA2', 'BRCA1'] 
# Результат: Unique genes: ['BRAF', 'KRAS', 'TP53', 'PIK3CA', 'EGFR', 'BRCA2', 'BRCA1'] 
# Repetitive genes: ['EGFR', 'BRCA1']

genes = ['BRCA1', 'TP53', 'EGFR', 'BRCA2', 'BRCA1', 'EGFR', 
         'KRAS', 'BRCA1', 'TP53', 'BRCA1', 'KRAS', 'EGFR', 'PIK3CA', 
         'BRCA1', 'TP53', 'BRAF', 'EGFR', 'BRCA2', 'BRCA2', 'BRCA1']

dobavit = input('Добавить новый ген?')
udalit = input('Удалить ген?')
if dobavit:
    genes.append(dobavit)
    print(genes)
if udalit:
    if udalit in genes:
        n = genes.index(udalit)
        genes.pop(n)
        print(genes)
    else:
        print("Нет такого гена!")

#1)
unique_genes = []
for gen in genes:
    if gen not in unique_genes:
        unique_genes.append(gen)
print("Unique genes:", unique_genes)        

repet_genes = []
for gen in genes:
    if genes.count(gen) > 3 and gen not in repet_genes:
        repet_genes.append(gen)        
print("Repetitive genes:", repet_genes)    
