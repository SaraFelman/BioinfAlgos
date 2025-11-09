import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import warnings
warnings.filterwarnings('ignore')

vaers_data = pd.read_csv('2023VAERSDATA.csv', encoding='latin1', low_memory=False)

# 1. Подсчёт мужчин и женщин
men_count = vaers_data[vaers_data['SEX'] == 'M'].shape[0] #.shape возвращает кортеж с двумя числами 0 - число строк
women_count = vaers_data[vaers_data['SEX'] == 'F'].shape[0]
unknown_sex_count = vaers_data.shape[0] - men_count - women_count
print(f"Мужчин: {men_count}")
print(f"Женщин: {women_count}")
print(f"Неизвестный пол: {unknown_sex_count}")

# 2. Возрастные группы
def age_group(age):
    if pd.isna(age):
        return 'Неизвестно'
    elif age <= 18:
        return '0-18'
    elif age <= 45:
        return '18-45'
    elif age <= 75:
        return '45-75'
    else:
        return '75+'

vaers_data['AGE_GROUP'] = vaers_data['AGE_YRS'].apply(age_group)
print("\nРаспределение по возрастным группам:")
print(vaers_data['AGE_GROUP'].value_counts()) #функция подсчета частоты каждой группы. Возвращает сортированный результат

# 3. Количество умерших (DIED - смерть после вакцинации). 
died_count = vaers_data[vaers_data['DIED'] == 'Y'].shape[0] # .shape[0] Берёт количество строк (отчётов)
print(f"\nУмерло: {died_count}")

# 4. Анализ умерших 
deceased = vaers_data[vaers_data['DIED'] == 'Y'] # Новый DF с умершими

# Процент с заболеванием на момент вакцинации
had_illness = deceased['CUR_ILL'].notna() & (deceased['CUR_ILL'].str.strip() != '') #не ноль и не пробел
illness_percent = (had_illness.sum() / died_count) * 100 if died_count > 0 else 0 #зашита от деление на 0
print(f"\nПроцент умерших с заболеванием на момент вакцинации: {illness_percent:.2f}%")

# Хронические + аллергия
had_chronic = deceased['HISTORY'].notna() & (deceased['HISTORY'].str.strip() != '')
had_allergy = deceased['ALLERGIES'].notna() & (deceased['ALLERGIES'].str.strip() != '')
chronic_and_allergy = (had_chronic & had_allergy).sum()
print(f"Умерших с хроническими болезнями и аллергией: {chronic_and_allergy}")

# Обращались за медпомощью
sought_help = deceased[
    (deceased['HOSPITAL'] == 'Y') | #Госпитализация после вакцинации
    (deceased['ER_ED_VISIT'] == 'Y') | #Неотложка / скорая
    (deceased['OFC_VISIT'] == 'Y') | #Визит к врачу / поликлиника
    (deceased['ER_VISIT'] == 'Y') #Старое поле (из VAERS 1) — то же, что ER_ED_VISIT
].shape[0] #количество таких случаев
print(f"Умерших, обращавшихся за медпомощью: {sought_help}")

# 5. Слияние с VAERSVAX
vaers_vax = pd.read_csv('2023VAERSVAX.csv', encoding='latin1', low_memory=False)
merged_data = pd.merge(vaers_data, vaers_vax, on='VAERS_ID', how='inner') #Объединение по общему айдишнику + только совпадающих
print("\nФорма объединённых данных:", merged_data.shape)

# 6. Вакцина + Больничный
hospitalized_by_vax = merged_data[merged_data['HOSPITAL'] == 'Y'].groupby('VAX_TYPE')['VAERS_ID'].count().sort_values(ascending=False) #фильтр только с госпитализацией + групп по типу вакцины + счет кол-во отчетов по ID + сорт по умемньшению
vax_with_most_hospital = hospitalized_by_vax.index[0] # берем наибольший индекс
hospital_count = hospitalized_by_vax.iloc[0] # берем наибольшее число случаев
print(f"\nТип вакцины с наибольшим числом госпитализаций: {vax_with_most_hospital} ({hospital_count} случаев)")

# 7. Посчитать, сколько людей в разных возрастных группах вакцинировались пероральным способом
# Пероральный = VAX_ROUTE == 'PO' (Per Oral, из Table 5)
oral_vax_by_age = merged_data[merged_data['VAX_ROUTE'] == 'PO'].groupby('AGE_GROUP')['VAERS_ID'].count()
print("\nВакцинации пероральным способом по возрастным группам:")
print(oral_vax_by_age)

# 8. Определить вакцину с наибольшей долей умерших
# Группируем по VAX_TYPE, считаем долю (умершие / общее число отчётов)
deaths_by_vax = merged_data.groupby('VAX_TYPE').agg({ 
    'VAERS_ID': 'count',  # Подсчет count для каждой вакцины
    'DIED': lambda x: (x == 'Y').sum()  # лямбда функция как цикл, который проходится по каждой вакцине и считает раз в столдце DIED стоит Y
}).rename(columns={'VAERS_ID': 'total_reports'}) #переименовываем поля
deaths_by_vax['death_rate'] = (deaths_by_vax['DIED'] / deaths_by_vax['total_reports']) * 100 #доля умерших
vax_with_highest_death_rate = deaths_by_vax['death_rate'].idxmax() # поиск максимума
highest_rate = deaths_by_vax.loc[vax_with_highest_death_rate, 'death_rate'] #.loc — это доступ к ячейке таблицы по метке строки и столбца
print(f"\nВакцина с наибольшей долей умерших: {vax_with_highest_death_rate} ({highest_rate:.4f}%)")

# 9. Найти вакцину (и её производителя) от COVID-19 с наименьшим числом побочных эффектов
# Побочные эффекты = общее число отчётов (adverse events)
# Фильтр COVID: VAX_TYPE.startswith('COVID')
covid_data = merged_data[merged_data['VAX_TYPE'].str.startswith('COVID', na=False)] #берем столбец + превращаем в строковый объект + проверяем что строка начинается с подстроки ковид
covid_by_vax_manu = covid_data.groupby(['VAX_TYPE', 'VAX_MANU'])['VAERS_ID'].count().reset_index(name='report_count') # # групп + посчет айдишника + превратить индекс в столбец + переименовать столбец = найти строку с минимальным отчетом
vax_manu_with_least_reports = covid_by_vax_manu.loc[covid_by_vax_manu['report_count'].idxmin()] # .loc[min_idx] — взять строку по индексу + .idxmin() — найти индекс минимума
print(f"\nCOVID-вакцина с наименьшим числом отчётов о побочных эффектах: {vax_manu_with_least_reports['VAX_TYPE']} от {vax_manu_with_least_reports['VAX_MANU']} ({vax_manu_with_least_reports['report_count']} отчётов)")

    ##Задание номер 8##

# Установка стиля
sns.set(style="whitegrid", font_scale=1.1)
plt.rcParams['figure.figsize'] = (10, 6)

# =============================================
# 1. Круговая диаграмма: распределение по полу
# =============================================
sex_counts = pd.Series({
    'Мужчины': men_count,
    'Женщины': women_count,
    'Неизвестно': unknown_sex_count
})

plt.figure(figsize=(8, 8))
plt.pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Распределение по полу в отчётах VAERS (2023)', fontsize=14, pad=20)
plt.axis('equal')
plt.show()
# =============================================
# 2. Столбчатая диаграмма: возрастные группы
# =============================================
age_group_counts = vaers_data['AGE_GROUP'].value_counts().reindex(['0-18', '18-45', '45-75', '75+', 'Неизвестно'])

plt.figure(figsize=(10, 6))
bars = plt.bar(age_group_counts.index, age_group_counts.values, color=sns.color_palette('viridis', len(age_group_counts)))
plt.title('Распределение по возрастным группам', fontsize=14)
plt.xlabel('Возрастная группа')
plt.ylabel('Количество отчётов')
plt.xticks(rotation=0)

# Подписи над столбцами
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
             f'{int(height)}', ha='center', va='bottom')

plt.tight_layout()
plt.show()
# =============================================
# 3. Тепловая карта корреляций
# =============================================
# Подготовка данных для корреляции
corr_data = vaers_data[['AGE_YRS', 'HOSPDAYS', 'HOSPITAL', 'AGE_GROUP']].copy()

# Преобразуем HOSPITAL: Y -> 1, иначе -> 0
corr_data['HOSPITAL'] = corr_data['HOSPITAL'].map({'Y': 1, 'N': 0}).fillna(0).astype(int)

# Преобразуем возрастные группы в числовой формат (середина диапазона)
age_group_map = {
    '0-18': 9,
    '18-45': 31.5,
    '45-75': 60,
    '75+': 85,
    'Неизвестно': np.nan
}
corr_data['AGE_GROUP_NUM'] = corr_data['AGE_GROUP'].map(age_group_map)

# Удаляем строки с пропусками в HOSPDAYS для корректной корреляции
corr_matrix = corr_data[['AGE_YRS', 'HOSPDAYS', 'HOSPITAL', 'AGE_GROUP_NUM']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, square=True, 
            linewidths=.5, cbar_kws={"shrink": .8}, fmt='.2f')
plt.title('Матрица корреляций: возраст, госпитализация, дни в больнице')
plt.tight_layout()
plt.show()
# =============================================
# 4. Диаграмма размаха (boxplot): ONSET_DATE для топ-5 вакцин по госпитализациям
# =============================================
# Преобразуем даты
merged_data['VAX_DATE'] = pd.to_datetime(merged_data['VAX_DATE'], errors='coerce')
merged_data['ONSET_DATE'] = pd.to_datetime(merged_data['ONSET_DATE'], errors='coerce')
merged_data['DAYS_TO_ONSET'] = (merged_data['ONSET_DATE'] - merged_data['VAX_DATE']).dt.days

# Берём топ-5 вакцин по числу госпитализаций
top5_vax = hospitalized_by_vax.head(5).index
boxplot_data = merged_data[merged_data['VAX_TYPE'].isin(top5_vax)].copy()
boxplot_data['VAX_TYPE'] = boxplot_data['VAX_TYPE'].replace({
    'COVID19': 'COVID-19',
    'COVID19-2': 'COVID-19 (2 дозы)',
    'VARZOS': 'Zoster',
    'FLU4': 'Грипп (4-вал.)',
    'PPV': 'Пневмо 23'
})

plt.figure(figsize=(12, 7))
sns.boxplot(data=boxplot_data, x='VAX_TYPE', y='DAYS_TO_ONSET', palette='Set2')
plt.title('Распределение дней от вакцинации до побочных эффектов\n(топ-5 вакцин по госпитализациям)', fontsize=14)
plt.xlabel('Тип вакцины')
plt.ylabel('Дней до проявления')
plt.ylim(0, boxplot_data['DAYS_TO_ONSET'].quantile(0.99))  # убираем выбросы
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
# =============================================
# 5. WordCloud: симптомы для вакцины с наименьшим числом побочек (из пункта 9)
# =============================================
# Находим VAERS_ID для вакцины с минимальным числом отчётов
target_vax_type = vax_manu_with_least_reports['VAX_TYPE']
target_manu = vax_manu_with_least_reports['VAX_MANU']

# Фильтруем данные по этой вакцине
symptom_data = merged_data[
    (merged_data['VAX_TYPE'] == target_vax_type) & 
    (merged_data['VAX_MANU'] == target_manu)
]

# Объединяем все симптомы в один текст
symptoms_text = ' '.join(symptom_data['SYMPTOM1'].fillna('') + ' ' + 
                         symptom_data['SYMPTOM2'].fillna('') + ' ' +
                         symptom_data['SYMPTOM3'].fillna('') + ' ' +
                         symptom_data['SYMPTOM4'].fillna('') + ' ' +
                         symptom_data['SYMPTOM5'].fillna(''))

# Создаём WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white', 
                      colormap='viridis', max_words=100, contour_width=1, 
                      contour_color='steelblue').generate(symptoms_text)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title(f'Облако слов: симптомы для {target_vax_type} ({target_manu})\n(наименьшее число побочек)', 
          fontsize=14, pad=20)
plt.tight_layout()
plt.show()