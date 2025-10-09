import os

def split_fasta(path):
    assert os.path.exists(path), f"Файл {path} не найден!"

    table_data = []
    lines = []
    with open(path, 'r') as in_file:
        for line in in_file:
            print(line)
            if line.startswith('>'):
                if lines:
                    first_part = lines[0].split()[0]
                    #lines[0] — это первая строка(заголовок) >sp|O78750|COX2_SHEEP Cytochrome c oxidase subunit 2 OS=Ovis aries OX=9940 GN=MT-CO2 PE=1 SV=1
                    #.split()[0] — берем до пробела   >sp|O78750|COX2_SHEEP
                    first_part = first_part.split('|')  #.split('|') — делю строку по |     ['>sp', 'P12345', 'COX1_HUMAN']
                    out_name = f'{first_part[1]}_{first_part[2]}.fasta'
                    with open(f'./fastas/{out_name}', 'w') as out_file:    #P12345_COX1_HUMAN.fasta
                        out_file.writelines(lines)    # и заголовок и последовательность в фасту

                    seq = ''.join(lines[1:]).replace('\n', '')     # берет строки, склеивает,  replace удаление переноса строк
                    table_data.append(
                        f'{first_part[1]}\t{len(seq)}\t{seq}\n'
                    )
                lines = [line]
            else:
                lines.append(line)

        if lines:
            first_part = lines[0].split()[0]
            first_part = first_part.split('|')
            out_name = f'{first_part[1]}_{first_part[2]}.fasta'
            with open(f'./fastas/{out_name}', 'w') as out_file:
                out_file.writelines(lines)

            seq = ''.join(lines[1:]).replace('\n', '')
            table_data.append(
                f'{first_part[1]}\t{len(seq)}\t{seq}\n'
            )

    with open('table.txt', 'w') as table:
        table.write('ID\tlength\tsequence\n')
        table.writelines(table_data)


split_fasta('/Users/fixed/PycharmProjects/BioinfAlgos/Week_5/cox1.fasta')