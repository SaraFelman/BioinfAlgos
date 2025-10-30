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

import numpy as np
import pandas as pd

# 0. Прочитать файл VAERSDATA.
vaerdata = pd.read_csv("2023VAERSDATA.csv", encoding="iso–8859–1")
vaerdata.set_index("VAERS_ID")
# print(vaerdata.head())

# # 1. Посчитать количество мужчин и женщин в выборке.
age_sex = vaerdata[["SEX"]].value_counts()
# print(age_sex.head())

# # 2. Добавить новый столбец с признаком разделения по возрастным группам:
# # 0-18; 18-45; 45-75; 75 и старше.
infants = vaerdata.loc[vaerdata["AGE_YRS"].isnull() & vaerdata["CAGE_MO"].notnull(), "Age_group"] = "0-18"
adult_names0 = vaerdata.loc[vaerdata["AGE_YRS"] < 18, "Age_group" ] = "0-18"
adult_names1 = vaerdata.loc[(vaerdata["AGE_YRS"] >= 18) & (vaerdata["AGE_YRS"] < 45), "Age_group" ] = "18-45"
adult_names2 = vaerdata.loc[(vaerdata["AGE_YRS"] >= 45) & (vaerdata["AGE_YRS"] < 75), "Age_group" ] = "45-75"
adult_names3 = vaerdata.loc[vaerdata["AGE_YRS"] >= 75, "Age_group" ] = "75+"
print(vaerdata.head())
# учесть младенцев месяцы

# 3. Определить, сколько человек умерло от побочных эффектов вакцин.
vaerdata['VAX_DATE'] = pd.to_datetime(vaerdata['VAX_DATE'])
vaerdata['end_date'] = pd.to_datetime(vaerdata['end_date'])
time_difference = vaerdata['end_date'] - vaerdata['start_date']
max_period = pd.Timedelta(days=30)
filtered_df = vaerdata[time_difference <= max_period]

died = vaerdata.loc[vaerdata["DIED"] == "Y" & vaerdata["DATEDIED"]] or vaerdata.loc[vaerdata["DIED"] == "Y" & vaerdata["DATEDIED"]]
# print(died.shape) дата смерти, угроза жизни, TODAYS_DATE


# 4. У какого процента умерших были заболевания на момент вакцинирования?
died_cur_ill = vaerdata.loc[vaerdata["CUR_ILL"].notnull() & vaerdata["DIED"] == "Y"].shape
died_cur_ill = died.loc[died["CUR_ILL"].notnull()]
cur_ill = vaerdata["CUR_ILL"]
# print(cur_ill[0:100])
# print("died", died.shape, "died WITH desiese", died_cur_ill.shape)
# print("У",(died_cur_ill.shape[0] * 100)/died.shape[0],"% умерших были заболевания на момент вакцинирования")
# округлить + убрать none

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
hospitalized = merged[merged["HOSPITAL"] == "Y"]
hospital_type = hospitalized["VAX_TYPE"].value_counts()
# print(hospital_type.head())
# проверить Disability если сильно много - вряд ли инвалиды, скорее больничный +мб они просто болели ковидом чекать симптом 2 в таблице симптомов
# процент посмотреть

# 7. Посчитать, сколько людей в разных возрастных группах вакцинировались
# пероральным способом.
PO = merged.loc[merged["VAX_ROUTE"] == "PO"]
# print(PO.shape)
# age_group добавить

# 8. Определить вакцину с наибольшей долей умерших.
# "VAX_NAME"
# all_vax =
# died_vax =
# vax = merged.loc[merged["VAX_NAME"] & merged["DEAD"] == "Y"]
# print()
# print((vax.shape[0]*100)/died.shape[0]).max())
grrp = merged.groupby("VAX_NAME")["DIED"].count().max()
print(grrp)

# # 9. Найти вакцину (и её производителя) от COVID-19 с наименьшим числом побочных эффектов.
# vaerssymptoms = pd.read_csv("2023VAERSSYMPTOMS.csv", encoding="iso–8859–1")
# merged3 = pd.merge(vaerdata, vaersvax, vaerssymptoms, on="VAERS_ID")
# print(merged3.head())

# covid = merged3[merged3["VAX_TYPE"] == "COVID19"]
# summary = (covid.groupby(["VAX_NAME", "VAX_MANU"])["symptom_count"]).mean()
# print(summary)

# symp1 = merged[merged["SYMPTOM1"].notnull()]
# vax_min_se = merged3.groupby(covid)[symp1].count().min()
# ковдных взять по вакцине, к ним симптомы,  проверить на бред в симптомах

