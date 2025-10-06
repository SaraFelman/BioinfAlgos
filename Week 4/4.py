# Задание 4. Баллы к коллоквиуму.
# Напишите программу, которая в строке, представляющей из себя 
# молекулярную формулу, подсчитывает количество всех атомов и возвращает 
# результат в виде словаря
# Пример:
# parse_molecule('H2O') --> {'H':2, 'O': 1}
# parse_molecule('Mg(OH)2') --> {'Mg':1, 'O': 2, 'H':2}
# parse_molecule('K4[NO(SO3)2]2') --> {'K':4, 'O': 14, 'N':2, 'S': 4}

def parse_molecule(molecule: str) -> dict[str, int]:
    mol_res = []

    is_inside_brackets = False
    for i in range(len(molecule)):
        if molecule[i] == '[':
            is_inside_brackets = True
            for j in range(i, len(molecule)):
                if molecule[j] == ']':
                    mol_res.append(molecule[i+1 : j] * int(molecule[j+1]))
                    break
        elif molecule[i] == ']':
            is_inside_brackets = False
        elif not is_inside_brackets and molecule[i-1] != ']':
            mol_res.append(molecule[i])

    molecule = ''.join(mol_res)
    mol_res = []
    is_inside_brackets = False
    for i in range(len(molecule)):
        if molecule[i] == '(':
            is_inside_brackets = True
            for j in range(i, len(molecule)):
                if molecule[j] == ')':
                    mol_res.append(molecule[i+1 : j] * int(molecule[j+1]))
                    break
        elif molecule[i] == ')':
            is_inside_brackets = False
        elif not is_inside_brackets and molecule[i-1] != ')':
            mol_res.append(molecule[i])

    molecule = ''.join(mol_res)
    ans: dict[str, int] = dict() #создаем пустой словарь 

    chem_elem = []
    for i in range(len(molecule)):
        if molecule[i].isupper():
            if chem_elem:
                if ''.join(chem_elem) in ans:
                    ans[''.join(chem_elem)] += 1
                else:
                    ans[''.join(chem_elem)] = 1
            chem_elem = [molecule[i]]

        if molecule[i].islower():
            chem_elem.append(molecule[i])
        
        if molecule[i].isdecimal():
            if chem_elem:
                if ''.join(chem_elem) in ans:
                    ans[''.join(chem_elem)] += int(molecule[i])
                else:
                    ans[''.join(chem_elem)] = int(molecule[i])
            chem_elem = []

    if chem_elem:
        if ''.join(chem_elem) in ans:
            ans[''.join(chem_elem)] += 1
        else:
            ans[''.join(chem_elem)] = 1

    return ans
    
# molecule = 'K4[NO(SO3)2]2Mn[H2O]3'

# TESTS
print(parse_molecule('H2O'))
# --> {'H':2, 'O': 1}
print(parse_molecule('Mg(OH)2'))
# --> {'Mg':1, 'O': 2, 'H':2}
print(parse_molecule('K4[NO(SO3)2]2'))
# --> {'K':4, 'O': 14, 'N':2, 'S': 4}
