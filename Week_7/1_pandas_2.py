import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud
import seaborn as sns

# 0. Прочитать файл VAERSDATA.
df = pd.read_csv('2023VAERSDATA.csv', encoding='iso–8859–1')
# df.set_index('VAERS_ID')
# print(df.head())

vaerdata = pd.read_csv("2023VAERSDATA.csv", encoding="iso–8859–1")
# vaerdata.set_index("VAERS_ID")

# 1. Посчитать количество мужчин и женщин в выборке.
# print(df[['SEX']].value_counts())

# 2. Добавить новый столбец с признаком разделения по возрастным группам: 0-18; 18-45; 45-75; 75 и старше.
df.loc[df['AGE_YRS'].isnull() & df['CAGE_MO'].notnull(), 'Age_group'] = '0-18'
df.loc[df['AGE_YRS'] < 18, 'Age_group'] = '0-18'
df.loc[df['AGE_YRS'].between(18, 44), 'Age_group'] = '18-45'
df.loc[df['AGE_YRS'].between(45, 74), 'Age_group'] = '45-75'
df.loc[df['AGE_YRS'] >= 75, 'Age_group'] = '75+'


# 3. Определить, сколько человек умерло от побочных эффектов вакцин.
df['VAX_DATE'] = pd.to_datetime(df['VAX_DATE'])
df['DATEDIED'] = pd.to_datetime(df['DATEDIED'])
time_difference = df['DATEDIED'] - df['VAX_DATE']  # Исправлено на правильные столбцы
min_period = pd.Timedelta(days=14)  # Изменено на 2 недели
filtered_df = df[(time_difference <= min_period) & (df['VAX_DATE'].notna()) & (df['DATEDIED'].notna())]  # Изменено условие

died = filtered_df.loc[filtered_df['DIED'] == 'Y']
# print(died.shape)
died2 = df.loc[df['DIED'] == 'Y']
# print(died2.head())

# died = vaerdata.loc[vaerdata['DIED'] == 'Y'] & vaerdata['DATEDIED']] or vaerdata.loc[vaerdata['DIED'] == 'Y' & vaerdata['DATEDIED']]
# print(died.shape) дата смерти, угроза жизни, TODAYS_DATE


# 4. У какого процента умерших были заболевания на момент вакцинирования?
# Тепловую карту из коэффициентов корреляции между возрастом,
# количеством дней госпитализации, возрастной группой, фактом
# госпитализации (пункт 4)
# died_cur_ill = vaerdata.loc[vaerdata['CUR_ILL'].notnull() & vaerdata['DIED'] == 'Y'].shape
# died_cur_ill = died.loc[died['CUR_ILL'].notnull()]
# cur_ill = vaerdata['CUR_ILL']
# print(cur_ill[0:100])
# print('died', died.shape, 'died WITH desiese', died_cur_ill.shape)
# 4. У какого процента умерших были заболевания на момент вакцинирования?
# died_cur_ill = df.loc[df['CUR_ILL'].notnull() & (df['DIED'] == 'Y')].shape
# died_cur_ill = died.loc[died['CUR_ILL'].notnull() &
#                         ~died['CUR_ILL'].str.contains(r'^\s*(?:null|unset\s*-\s*0|N/A|NO?$|Na$|NONE?/.*|Not|Nothing)',
#                         case=False, na=False, regex=True)]
# cur_ill = df['CUR_ILL']
# print(cur_ill[0:100])
# print('died', died.shape, 'died WITH desiese', died_cur_ill.shape)
# print('У', round((died_cur_ill.shape[0] * 100)/died.shape[0], 2), '% умерших были заболевания на момент вакцинирования')
# округлить + убрать none

# 4. У какого процента умерших были заболевания на момент вакцинирования?
# Тепловую карту из коэффициентов корреляции между возрастом,
# количеством дней госпитализации, возрастной группой, фактом госпитализации (пункт 4)
died_cur_ill = df.loc[df['CUR_ILL'].notnull() & (df['DIED'] == 'Y')].shape
died_cur_ill = died.loc[died['CUR_ILL'].notnull() &
                        ~died['CUR_ILL'].str.contains(r'^\s*(?:null|unset\s*-\s*0|N/A|NO?$|Na$|NONE?/.*|Not|Nothing)',
                        case=False, na=False, regex=True)]
cur_ill = df['CUR_ILL']

# Тепловая карта корреляций
sns.set_theme()
corr_data = died[['AGE_YRS', 'HOSPDAYS', 'HOSPITAL', 'Age_group']].copy()
# print(corr_data.head())

# Преобразуем бинарные переменные в числовой формат
corr_data['HOSPITAL_NUM'] = corr_data['HOSPITAL'].map({'Y': 1}).fillna(0)

# Преобразуем возрастные группы в числовой формат
corr_data['AGE_GROUP_NUM'] = corr_data['Age_group'].map({'0-18': 0, '18-45': 1, '45-75': 2, '75+': 3})


numeric_cols = ['AGE_YRS', 'HOSPDAYS', 'HOSPITAL_NUM', 'AGE_GROUP_NUM']
correlation_matrix = corr_data[numeric_cols].corr()

# Переименовываем для понятности на графике - используем правильные названия столбцов
correlation_matrix.columns = ['Возраст', 'Дни госпитализации', 'Госпитализация', 'Возрастная группа']
correlation_matrix.index = ['Возраст', 'Дни госпитализации', 'Госпитализация', 'Возрастная группа']

# Построение тепловой карты
f, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', center=0, linewidths=.5, ax=ax)
plt.title('Тепловая карта корреляций среди умерших пациентов')
plt.tight_layout()
# plt.show()


# У скольки из них были хронические заболевания вместе с аллергией в анамнезе?
HISTORY_ALLERGIES = died.loc[died['HISTORY'].notnull() & died['ALLERGIES'].notnull()]
# print('HISTORY_ALLERGIES', HISTORY_ALLERGIES.shape)
# print('У', (HISTORY_ALLERGIES.shape[0]*100)/died.shape[0], '% из умерших были хронические и аллергии')

# Сколько из них обратилось за медицинской помощью после вакцинации?
visits = died.loc[died['ER_ED_VISIT'].notnull() & died['OFC_VISIT'].notnull()]
# print((visits.shape[0]*100)/died.shape[0], '% человек из числа умерших обратилось за медицинской помощью')
# hospitalased добавить проверить мб уже внутри

# 5. Объединить данные с информацией из таблицы VAERSVAX.
vaersvax = pd.read_csv('2023VAERSVAX.csv', encoding='iso–8859–1')
# vaersvax.set_index('VAERS_ID')
merged = pd.merge(df, vaersvax, on='VAERS_ID')
# print(merged.info())
# print(merged.head())
# уточнить что по айди один и тот же человек, а не 3 прививки одному


# 6. Определить тип вакцины, после которой больше всего людей брало больничный.
# hospitalized = merged[merged['HOSPITAL'] == 'Y']
# hospital_type = hospitalized['VAX_TYPE'].value_counts()
# print(hospital_type.head())
# проверить Disability если сильно много - вряд ли инвалиды, скорее больничный +мб они просто болели ковидом чекать симптом 2 в таблице симптомов
# процент посмотреть
hospitalized = merged[merged['HOSPITAL'] == 'Y']
hospital_type = hospitalized['VAX_TYPE'].value_counts()
vaccinated = merged['VAX_TYPE'].value_counts()
hospital_type_percent = (hospital_type/vaccinated * 100).round(2).fillna(0)
# print(hospital_type_percent.sort_values(ascending=False))

# Диаграммы размаха количества дней от факта вакцинации до проявления
# побочных эффектов для пяти типов вакцин (пункт 6)
merged.dropna(subset=['VAX_DATE', 'ONSET_DATE'], inplace=True)
merged['VAX_DATE'] = pd.to_datetime(merged['VAX_DATE'])
merged["ONSET_DATE"] = pd.to_datetime(merged['ONSET_DATE'])
time_difference = merged['ONSET_DATE'] - merged['VAX_DATE']
time_difference = time_difference.apply(lambda x: x.days)
# print(time_difference)

labels = ['MU', 'MEA', 'PNC', 'SMALL', 'COVID19']
colors = ['peachpuff', 'orange', 'tomato', 'salmon', 'maroon']
data_razmaha = [
    time_difference[(merged['VAX_TYPE'] == label) & (merged['HOSPITAL'] == 'Y') & (time_difference >= 0)] #merged[merged. <= 0]
    for label in labels
]


fig, ax = plt.subplots()
ax.set_ylabel('Дни от вакцинации до проявления побочных эффектов')

bplot = ax.boxplot(data_razmaha,
                   patch_artist=True,  # fill with color
                   tick_labels=labels,
                   showfliers=False
)  # will be used to label x-ticks

# fill with colors
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
# plt.show()

# 7. Посчитать, сколько людей в разных возрастных группах вакцинировались
# пероральным способом.
po = merged.loc[merged['VAX_ROUTE'] == 'PO']
po_age_counts = po['Age_group'].value_counts()
# print(po_age_counts)
# age_group добавить ДОБАВИЛА

# 8. Определить вакцину с наибольшей долей умерших.
merged.dropna(subset=['AGE_YRS', 'VAX_NAME'], inplace=True)
merged.loc[merged['DIED'] == 'Y', 'DIED'] = 1
merged.loc[merged['DIED'] != 1, 'DIED'] = 0

merged_8 = merged.groupby('VAX_NAME').agg({'DIED': 'sum'}).div(merged.groupby('VAX_NAME').size().to_frame('DIED'))

# print(merged_8.sort_values(by='DIED', ascending=False))

# # 9. Найти вакцину (и её производителя) от COVID-19 с наименьшим числом побочных эффектов.
vaerssymptoms = pd.read_csv('2023VAERSSYMPTOMS.csv', encoding='iso–8859–1')
merged3 = pd.merge(merged, vaerssymptoms, on='VAERS_ID')

covid = merged3[merged3['VAX_TYPE'] == 'COVID19']
symp1 = covid[covid['SYMPTOM1'] != "No adverse event"]
min_pobochki = symp1['VAX_NAME'].value_counts()
vaccinated_covid = covid['VAX_NAME'].value_counts()
print(min_pobochki)
min_pobochki_percent = (min_pobochki/vaccinated_covid * 100).round(2).fillna(0)
print(min_pobochki_percent.sort_values(ascending=True))


# symp1 = merged[merged['SYMPTOM1'].notnull()]
# vax_min_se = merged3.groupby(covid)[symp1].count().min()
# ковдных взять по вакцине, к ним симптомы, проверить на бред в симптомах
# hospitalized = merged[merged['HOSPITAL'] == 'Y']
# hospital_type = hospitalized['VAX_TYPE'].value_counts()
# vaccinated = merged['VAX_TYPE'].value_counts()

# 5. Диаграмму WordCloud (библиотека wordcloud) для вакцины из пункта 9.
# text = [symp1['VAX_NAME'] == "COVID19 (COVID19 (PFIZER-BIONTECH))"]
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
from wordcloud import STOPWORDS

# Фильтруем данные для нужной вакцины
covid_data = symp1[symp1['VAX_NAME'] == "COVID19 (COVID19 (PFIZER-BIONTECH))"]

# Собираем симптомы из одного столбца
text = ' '.join(covid_data['SYMPTOM1'].dropna().astype(str))

stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height=400).generate(text)
plt.figure(figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title('Облако слов симптомов для вакцины COVID19 (PFIZER-BIONTECH)')
plt.show()


# Диаграммы
# Круговая диаграмма к пункту 1.
vals = df[['SEX']].value_counts()
labels = ['F', 'M', 'U']
fig, ax = plt.subplots()
ax.pie(vals, labels=labels)
ax.axis('equal')
plt.savefig('1.png')
# plt.close()

# Столбчатая диаграмма к пункту 2.
ax = df.groupby(['Age_group']).size().plot.bar(x='Age_group', y='size', rot=0)
ax.set_title('Количество людей по возрастным группам')
ax.set_xlabel('Возрастная группа')
ax.set_ylabel('Количество людей')
plt.savefig('2.png')
# plt.close()
