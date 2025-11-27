from ba2c import profile_kmer

from random import randint
from copy import deepcopy
# для создания полной копии сложных объектов (списков списков)

def calc_profile(motifs: list[str]) -> list[list[float]]:
    n: int = len(motifs[0])
    t: int = len(motifs)
    counts: list[list[float]] = [[0 for _ in range(n)] for _ in range(4)]
    # Создает матрицу 4×n, заполненную нулями. Каждая строка соответствует нуклеотиду (A, C, G, T), каждый столбец - позиции в мотиве
    for j in range(n):
    # Внешний цикл по всем позициям в мотиве (от 0 до n-1)
        for i in range(t):
        # Внутренний цикл по всем мотивам в списке.
            if motifs[i][j] == "A":
                counts[0][j] += 1/t
            elif motifs[i][j] == 'C':
                counts[1][j] += 1/t
            elif motifs[i][j] == 'G':
                counts[2][j] += 1/t
            elif motifs[i][j] == 'T':
                counts[3][j] += 1/t
    return counts
# Для каждого нуклеотида в позиции j мотива i увеличивает соответствующую
# ячейку в матрице counts на 1/t (нормализация).

def calc_score(motifs: list[str]) -> int:
    n: int = len(motifs[0]) #длина каждого мотива (все мотивы одинаковой длины)
    t: int = len(motifs) #количество мотивов в списке

    counts: list[list[float]] = [[0 for _ in range(n)] for _ in range(4)]
    # Создает матрицу 4×n, заполненную нулями. Каждая строка соответствует нуклеотиду (A, C, G, T), каждый столбец - позиции в мотиве
    for j in range(n):
    #Внешний цикл по всем позициям в мотиве (от 0 до n-1)
        for i in range(t):
        #Внутренний цикл по всем мотивам в списке.
            if motifs[i][j] == "A":
                counts[0][j] += 1
            elif motifs[i][j] == 'C':
                counts[1][j] += 1
            elif motifs[i][j] == 'G':
                counts[2][j] += 1
            elif motifs[i][j] == 'T':
                counts[3][j] += 1
# Заполняет матрицу counts абсолютными частотами (без нормализации).
    score: int = t * n #Инициализирует score максимально возможным значением (общее количество нуклеотидов во всех мотивах).
    for i in range(n):
        score -= max(
            counts[0][i],
            counts[1][i],
            counts[2][i],
            counts[3][i]
        )
#Для каждой позиции вычитает из score максимальную частоту нуклеотида в этой позиции.
#Таким образом, score уменьшается, когда в позициях есть консенсус.
    return score


def randomized_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    n: int = len(dna[0])
    #  randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    best_motifs: list[str] = [
        dna[randint(0, len(dna) - 1)][(start_ind := randint(0, n - k)):start_ind + k]
        for _ in range(t)
    ]
#
# best_motifs = []
# for i in range(t):
#     random_dna_index = randint(0, len(dna) - 1)
#     random_dna_string = dna[random_dna_index]
#     start_position = randint(0, n - k)
#     random_kmer = random_dna_string[start_position:start_position + k]
#     best_motifs.append(random_kmer)

#randint(0, len(dna) - 1) - случайно выбирает строку из dna
#randint(0, n - k) - случайно выбирает начальную позицию
#start_ind + k - конечная позиция k-mer
#Используется walrus operator := для сохранения значения

    # BestMotifs ← Motifs
    motifs: list[str] = deepcopy(best_motifs)
    # Создает глубокую копию best_motifs для текущей итерации
    # a = [ i  for i in range(10)]
    # a = []
    # for i in range(10):
    #     a.append(i)
    # print(best_motifs)

    #создали столько спиcков сколько len(dna) = [[] for _ in range(len(dna))]
    # random_kmer = randint(0, n - k + 1)
    # string
    while True:
        profile = calc_profile(motifs) #Вычисляет профильную матрицу для текущих мотивов.
        motifs: list[str] = [] #Очищает список motifs для нового набора.

        for i in dna:
            curr_motif = profile_kmer(i, k, *profile)
            motifs.append(curr_motif)
#Для каждой DNA-строки находит наиболее вероятный k-mer на основе профиля и добавляет его в motifs.

        if calc_score(motifs) < calc_score(best_motifs):
            best_motifs = motifs
        else:
            return best_motifs
#Если новый набор мотивов лучше (имеет меньший score), обновляет best_motifs

def laplace(dna: list[str], k: int, t: int) -> list[str]:
    best_motifs = randomized_motif_search(dna, k, t) #Получает начальный набор мотивов.
    for _ in range(5000):
        motifs = randomized_motif_search(dna, k, t)
        if calc_score(motifs) < calc_score(best_motifs):
            best_motifs = motifs
#5000 раз запускает алгоритм и сохраняет лучший результат.
    return best_motifs


k, t = map(int, input().split())
dna: list[str] = [input().strip() for _ in range(t)]
#Читает t DNA-строк, удаляя лишние пробелы.

# print(*calc_profile(dna), sep="\n")

print(*laplace(dna, k, t), sep='\n')
#  * распаковка
