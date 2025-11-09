# Задание 7.
# При помощи библиотек pandas и numpy, данных из архива 2022VAERSData
# и инструкции в файле VAERSDataUseGuide_en_September2023:
# 0. Прочитать файл VAERSDATA.
# 1. Посчитать количество мужчин и женщин в выборке.
# 2. Добавить новый столбец с признаком разделения по возрастным группам:
# 0-18; 18-45; 45-75; 75 и старше.
# 3. Определить, сколько человек умерло от побочных эффектов вакцин.
# 4. У какого процента умерших были заболевания на момент вакцинирования?
# У скольки из них были хронические заболевания вместе с аллергией в анамнезе?
# Сколько из них обратилось за медицинской помощью после вакцинации?
# 5. Объединить данные с информацией из таблицы VAERSVAX.
# 6. Определить тип вакцины, после которой больше всего людей брало больничный.
# 7. Посчитать, сколько людей в разных возрастных группах вакцинировались
# пероральным способом.
# 8. Определить вакцину с наибольшей долей умерших.
# 9. Найти вакцину (и её производителя) от COVID-19 с наименьшим числом побочных эффектов.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 0. Прочитать файл VAERSDATA.
vaerdata = pd.read_csv("2023VAERSDATA.csv", encoding="iso–8859–1")
vaerdata.set_index("VAERS_ID")
# print(vaerdata.head())

# # 1. Посчитать количество мужчин и женщин в выборке.
age_sex = vaerdata[["SEX"]].value_counts()
# print(age_sex.head())

vals = vaerdata[["SEX"]].value_counts()
labels = ["F", "M", "U"]
fig, ax = plt.subplots()
ax.pie(vals, labels=labels)
ax.axis("equal")
# plt.show()

# # 2. Добавить новый столбец с признаком разделения по возрастным группам:
# # 0-18; 18-45; 45-75; 75 и старше.
infants = vaerdata.loc[vaerdata["AGE_YRS"].isnull() & vaerdata["CAGE_MO"].notnull(), "Age_group"] = "0-18"
adult_names0 = vaerdata.loc[vaerdata["AGE_YRS"] < 18, "Age_group" ] = "0-18"
adult_names1 = vaerdata.loc[(vaerdata["AGE_YRS"] >= 18) & (vaerdata["AGE_YRS"] < 45), "Age_group" ] = "18-45"
adult_names2 = vaerdata.loc[(vaerdata["AGE_YRS"] >= 45) & (vaerdata["AGE_YRS"] < 75), "Age_group" ] = "45-75"
adult_names3 = vaerdata.loc[vaerdata["AGE_YRS"] >= 75, "Age_group" ] = "75+"
comboo = adult_names0 + infants
# print(vaerdata.head())


categories = ["0-18", "18-45", "45-75", "75+"]
values = [comboo, adult_names1, adult_names2, adult_names3]
plt.bar(categories, values)
plt.title('Пример столбчатой диаграммы')
plt.xlabel('Категории')
plt.ylabel('Значения')
# plt.show()

# 3. Определить, сколько человек умерло от побочных эффектов вакцин.
vaerdata['VAX_DATE'] = pd.to_datetime(vaerdata['VAX_DATE'])
vaerdata['DATEDIED'] = pd.to_datetime(vaerdata['DATEDIED'])  # Исправлено на DATEDIED
time_difference = vaerdata['DATEDIED'] - vaerdata['VAX_DATE']  # Исправлено на правильные столбцы
min_period = pd.Timedelta(days=14)  # Изменено на 2 недели
filtered_df = vaerdata[(time_difference <= min_period) & (vaerdata['VAX_DATE'].notna()) & (vaerdata['DATEDIED'].notna())]  # Изменено условие

died = filtered_df.loc[filtered_df["DIED"] == "Y"]
# print(died.shape)
died2 = vaerdata.loc[vaerdata["DIED"] == "Y"]
# print(died2.shape)

# died = vaerdata.loc[vaerdata["DIED"] == "Y"] & vaerdata["DATEDIED"]] or vaerdata.loc[vaerdata["DIED"] == "Y" & vaerdata["DATEDIED"]]
# print(died.shape) дата смерти, угроза жизни, TODAYS_DATE


# 4. У какого процента умерших были заболевания на момент вакцинирования?
# Тепловую карту из коэффициентов корреляции между возрастом,
# количеством дней госпитализации, возрастной группой, фактом
# госпитализации (пункт 4)
# died_cur_ill = vaerdata.loc[vaerdata["CUR_ILL"].notnull() & vaerdata["DIED"] == "Y"].shape
# died_cur_ill = died.loc[died["CUR_ILL"].notnull()]
# cur_ill = vaerdata["CUR_ILL"]
# print(cur_ill[0:100])
# print("died", died.shape, "died WITH desiese", died_cur_ill.shape)
# 4. У какого процента умерших были заболевания на момент вакцинирования?
died_cur_ill = vaerdata.loc[vaerdata["CUR_ILL"].notnull() & (vaerdata["DIED"] == "Y")].shape
died_cur_ill = died.loc[died["CUR_ILL"].notnull() &
                        ~died["CUR_ILL"].str.contains(r'^\s*(?:null|unset\s*-\s*0|N/A|NO?$|Na$|NONE?/.*|Not|Nothing)',
                        case=False, na=False, regex=True)]
cur_ill = vaerdata["CUR_ILL"]
# print(cur_ill[0:100])
# print("died", died.shape, "died WITH desiese", died_cur_ill.shape)
# print("У", round((died_cur_ill.shape[0] * 100)/died.shape[0], 2), "% умерших были заболевания на момент вакцинирования")
# округлить + убрать none

sns.set_theme()
corr_data = died_cur_ill[['AGE_YRS', 'NUMDAYS', 'HOSPITAL', 'CUR_ILL']].copy()

numeric_cols = ['AGE_YRS', 'NUMDAYS', 'HOSPITAL', 'CUR_ILL']
correlation_matrix = corr_data[numeric_cols].corr()

# Переименовываем для понятности на графике
correlation_matrix.columns = ['Возраст', 'Дни госпитализации', 'Госпитализация', 'Возрастная группа', 'Заболевания']
correlation_matrix.index = ['Возраст', 'Дни госпитализации', 'Госпитализация', 'Возрастная группа', 'Заболевания']

# # Load the example flights dataset and convert to long-form
# flights_long = sns.load_dataset("flights")
# flights = (
#     flights_long
#     .pivot(index="month", columns="year", values="passengers")
# )
#
# # Draw a heatmap with the numeric values in each cell
# f, ax = plt.subplots(figsize=(9, 6))
# sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)

# У скольки из них были хронические заболевания вместе с аллергией в анамнезе?
HISTORY_ALLERGIES = died.loc[died["HISTORY"].notnull() & died["ALLERGIES"].notnull()]
# print("HISTORY_ALLERGIES", HISTORY_ALLERGIES.shape)
# print("У", (HISTORY_ALLERGIES.shape[0]*100)/died.shape[0], "% из умерших были хронические и аллергии")

# Сколько из них обратилось за медицинской помощью после вакцинации?
visits = died.loc[died["ER_ED_VISIT"].notnull() & died["OFC_VISIT"].notnull()]
# print((visits.shape[0]*100)/died.shape[0], "% человек из числа умерших обратилось за медицинской помощью")
# hospitalased добавить проверить мб уже внутри

# 5. Объединить данные с информацией из таблицы VAERSVAX.
vaersvax = pd.read_csv("2023VAERSVAX.csv", encoding="iso–8859–1")
vaersvax.set_index("VAERS_ID")
merged = pd.merge(vaerdata, vaersvax, on="VAERS_ID")
# print(merged.info())
# print(merged.head())
# уточнить что по айди один и тот же человек, а не 3 прививки одному


# 6. Определить тип вакцины, после которой больше всего людей брало больничный.
# Диаграммы размаха количества дней от факта вакцинации до проявления
# побочных эффектов для пяти типов вакцин (пункт 6)
hospitalized = merged[merged["HOSPITAL"] == "Y"]
hospital_type = hospitalized["VAX_TYPE"].value_counts()
# print(hospital_type.head())
# проверить Disability если сильно много - вряд ли инвалиды, скорее больничный +мб они просто болели ковидом чекать симптом 2 в таблице симптомов
# процент посмотреть

# 7. Посчитать, сколько людей в разных возрастных группах вакцинировались
# пероральным способом.
po = merged.loc[merged["VAX_ROUTE"] == "PO"]
po_age_counts = po["Age_group"].value_counts()
# print(po_age_counts)
# age_group добавить ДОБАВИЛА

# 8. Определить вакцину с наибольшей долей умерших.
died_type = died["VAX_NAME"].value_counts()  # По названию вакцины
total_type = vaervax["VAX_NAME"].value_counts()  # Общее количество по названию вакцины
# print(died_type)
# print(total_type)
# # Вычисляем долю умерших для каждой вакцины
# died_percent = (died_type / total_type * 100).fillna(0).round(2)
#
# # Находим вакцину с максимальной долей умерших
# max_percent_vaccine = died_percent.idxmax()
# max_percent_value = died_percent.max()
#
# print("Вакцина с наибольшей долей умерших:")
# print(max_percent_vaccine, ":", max_percent_value, "%")
# grrp = merged.groupby("VAX_NAME")["DIED"].count().max()
# print(grrp)

# # 9. Найти вакцину (и её производителя) от COVID-19 с наименьшим числом побочных эффектов.
# # 5. Диаграмму WordCloud (библиотека wordcloud) для вакцины из пункта 9.
# vaerssymptoms = pd.read_csv('2023VAERSSYMPTOMS.csv', encoding='iso–8859–1')
# merged3 = pd.merge(vaerdata, vaersvax, vaerssymptoms, on='VAERS_ID')
# print(merged3.head())
#
# covid = merged3[merged3['VAX_TYPE'] == 'COVID19']
# summary = (covid.groupby(['VAX_NAME', 'VAX_MANU'])['symptom_count']).mean()
# print(summary)
#
# symp1 = merged[merged['SYMPTOM1'].notnull()]
# vax_min_se = merged3.groupby(covid)[symp1].count().min()
# # ковдных взять по вакцине, к ним симптомы,  проверить на бред в симптомах

# 5. Диаграмму WordCloud (библиотека wordcloud) для вакцины из пункта 9.
vaerssymptoms = pd.read_csv('2023VAERSSYMPTOMS.csv', encoding='iso–8859–1')
merged3 = pd.merge(vaerdata, vaersvax, vaerssymptoms, on='VAERS_ID')
# print(merged3.head())

covid = merged3[merged3['VAX_TYPE'] == 'COVID19']
summary = (covid.groupby(['VAX_NAME', 'VAX_MANU'])['symptom_count']).mean()
# print(summary)

symp1 = merged[merged['SYMPTOM1'].notnull()]
vax_min_se = merged3.groupby(covid)[symp1].count().min()


# vaerssymptoms = pd.read_csv("2023VAERSSYMPTOMS.csv", encoding="iso–8859–1")
# merged3 = pd.merge(vaerdata, vaersvax, vaerssymptoms, on="VAERS_ID")
# print(merged3.head())

# covid = merged3[merged3["VAX_TYPE"] == "COVID19"]
# summary = (covid.groupby(["VAX_NAME", "VAX_MANU"])["symptom_count"]).mean()
# print(summary)

# symp1 = merged[merged["SYMPTOM1"].notnull()]
# vax_min_se = merged3.groupby(covid)[symp1].count().min()
# ковдных взять по вакцине, к ним симптомы,  проверить на бред в симптомах

