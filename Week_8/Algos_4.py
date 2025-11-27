
Pattern = input()
Text = input()
d = int(input())

def hamming(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Строки должны иметь одинаковую длину")
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance
# if hamming(Text, Pattern) <= d
