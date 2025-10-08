# Задание 5.
# Вывести на экран список с последовательностью с самым разнообразным 
# составом. В данном случае разнообразие будем считать по числу различных 
# аминокислот. Если наиболее разнообразных последовательностей несколько, 
# то выведите их все.
# Входные данные:
# protein_sequences = [
# 'MKFLSFVSTGLTLYP',
# 'MRLITALLLLAGASL',
# 'MSVGTALAGTITGIL',
# 'MSTVGRVAKALRKRA'
# ]
# Результат: ['MKFLSFVSTGLTLYP']
# Входные данные:
# protein_sequences = [
# 'MKLLSMVSTGLTLYP',

# 'MRLITALLLLAGASL',
# 'MSGGTALAGTITGIL',
# 'MSTVGRVAKALRKRA'
# ]
# Результат: ['MKLLSMVSTGLTLYP', 'MSTVGRVAKALRKRA']

protein_sequences =  [ 'MKFLSFVSTGLTLYP', 'MRLITALLLLAGASL', 'MSVGTALAGTITGIL', 'MSTVGRVAKALRKRA' ] 
#protein_sequences =  [ 'MKLLSMVSTGLTLYP', 'MRLITALLLLAGASL', 'MSGGTALAGTITGIL', 'MSTVGRVAKALRKRA' ]
max_m = 0 
uniq_seq = []
for seq in protein_sequences:
    a = [] # набираем уникальные аминок-ты
    for amino in seq:
        if amino not in a:
            a.append(amino)
                
    len_a = len(a)
    if len_a > max_m:
        max_m = len_a
        uniq_seq = [seq]
    elif len_a == max_m:
        uniq_seq.append(seq) 
print(uniq_seq)                 
