import streamlit as st
from catboost import CatBoostRegressor
import numpy as np
import json



base_skills_1 = ['Дополнительные льготы','Сварка без конкретизации вида/оборудования','Дуговая сварка','Удостоверения','Ручная сварка']
base_skills_2 = ['НАКС','Требования к образованию','Дополнительные льготы','Сварка без конкретизации вида/оборудования','Дуговая сварка','Удостоверения','Ручная сварка',]
m2_order = ['Сварка в среде аргона (РАД)\u200b', 'Обязательная сертификация', 'Обучение/профподготовка в компании', 'Плазменная сварка', 'Плазменная резка', 'Знания предметных областей для сварщика', 'Сборка и монтаж', 'Знание документации, проектов, чертежей, схем', 'Наплавка', 'Газовая сварка', 'Сварка в среде защитного газа', 'Знание правил безопасности', 'Знание техник, технологии сварки, наплавки', 'Газовая резка', 'Дуговая резка', 'Знание  устройств и правил эксплуатации сварочных аппаратов, машин', 'Настройка сварочного оборудования', 'Строгание', 'Строжка', 'Ручная резка', 'Бензо- и керосино- резание', 'Механизированная сварка', 'Автоматическая сварка', 'Резка', 'Обслуживание и ремонт сварочного оборудования', 'Действия перед/после сварки, резки', 'Контактная сварка', 'Чтение чертежей, документации', 'Соблюдение охраны труда, техники безопасности и пожарной безопасности', 'Контроль  сварки/резки, измерение', 'Пайка', 'Простые и средней сложности инструменты (изготовление, регулировка и ремонт)', 'Изготовление, регулировка и регулировка (простые узлы и средней сложности механизмы)', 'region_name_cat']
m01_order = ['Сварка в среде аргона (РАД)\u200b', 'НАКС', 'Обязательная сертификация', 'Обучение/профподготовка в компании', 'Требования к образованию', 'Плазменная сварка', 'Плазменная резка', 'Знания предметных областей для сварщика', 'Сборка и монтаж', 'Знание документации, проектов, чертежей, схем', 'Наплавка', 'Газовая сварка', 'Сварка в среде защитного газа', 'Знание правил безопасности', 'Знание техник, технологии сварки, наплавки', 'Газовая резка', 'Дуговая резка', 'Знание  устройств и правил эксплуатации сварочных аппаратов, машин', 'Настройка сварочного оборудования', 'Строгание', 'Строжка', 'Ручная резка', 'Бензо- и керосино- резание', 'Механизированная сварка', 'Автоматическая сварка', 'Резка', 'Обслуживание и ремонт сварочного оборудования', 'Действия перед/после сварки, резки', 'Контактная сварка', 'Чтение чертежей, документации', 'Соблюдение охраны труда, техники безопасности и пожарной безопасности', 'Контроль  сварки/резки, измерение', 'Пайка', 'Простые и средней сложности инструменты (изготовление, регулировка и ремонт)', 'Изготовление, регулировка и регулировка (простые узлы и средней сложности механизмы)', 'region_name_cat']


model_0_code_experience_is_vahta_sorted = json.load('model_0_code_experience_is_vahta_sorted.json').keys()
model_1_code_experience_is_vahta_sorted = json.load('model_1_code_experience_is_vahta_sorted.json').keys()
model_2_code_experience_is_vahta_sorted = json.load('model_2_code_experience_is_vahta_sorted.json').keys()
model_0_code_experience_isnt_vahta_sorted = json.load('model_0_code_experience_isnt_vahta_sorted.json').keys()
model_1_code_experience_isnt_vahta_sorted = json.load('model_1_code_experience_isnt_vahta_sorted.json').keys()
model_2_code_experience_isnt_vahta_sorted = json.load('model_2_code_experience_isnt_vahta_sorted.json').keys()


model_0_code_experience_is_vahta_sorted_mask = [model_0_code_experience_is_vahta_sorted.index(model_0_code_experience_is_vahta_sorted[i]) for i in range(36)]
model_0_code_experience_isnt_vahta_sorted_mask = [model_0_code_experience_is_vahta_sorted.index(model_0_code_experience_isnt_vahta_sorted[i]) for i in range(36)]
model_1_code_experience_is_vahta_sorted_mask = [model_0_code_experience_is_vahta_sorted.index(model_1_code_experience_is_vahta_sorted[i]) for i in range(36)]
model_1_code_experience_isnt_vahta_sorted_mask = [model_0_code_experience_is_vahta_sorted.index(model_1_code_experience_isnt_vahta_sorted[i]) for i in range(36)]
model_2_code_experience_is_vahta_sorted_mask = [model_0_code_experience_is_vahta_sorted.index(model_2_code_experience_is_vahta_sorted[i]) for i in range(34)]
model_2_code_experience_isnt_vahta_sorted_mask = [model_0_code_experience_is_vahta_sorted.index(model_2_code_experience_isnt_vahta_sorted[i]) for i in range(34)]

st.header("Предсказание зарплаты по вакансии сварщика исходя из навыков")
# data = pd.read_csv("fish.csv")

model_0_code_experience_is_vahta = CatBoostRegressor()
model_0_code_experience_is_vahta.load_model('model_0_code_experience_is_vahta')
model_0_code_experience_isnt_vahta = CatBoostRegressor()
model_0_code_experience_isnt_vahta.load_model('model_0_code_experience_isnt_vahta')
model_1_code_experience_is_vahta = CatBoostRegressor()
model_1_code_experience_is_vahta.load_model('model_1_code_experience_is_vahta')
model_1_code_experience_isnt_vahta = CatBoostRegressor()
model_1_code_experience_isnt_vahta.load_model('model_1_code_experience_isnt_vahta')
model_2_code_experience_is_vahta = CatBoostRegressor()
model_2_code_experience_is_vahta.load_model('model_2_code_experience_is_vahta')
model_2_code_experience_isnt_vahta = CatBoostRegressor()
model_2_code_experience_isnt_vahta.load_model('model_2_code_experience_isnt_vahta')



st.subheader("Выберите класс вакансии")
left_column, right_column = st.columns(2)
with left_column:
    inp_species = st.radio(
        'Наименование вакансии',
        np.unique(['Сварщик']))



st.subheader("Выберите стаж работы")
left_column1, right_column1 = st.columns(2)
with left_column1:
    experience = st.radio(
        'опыт работы:',
        np.unique(['Без опыта', 'От 1 до 3 лет','От 3 лет']))

f = open('regions_final.json')
data = json.load(f)

st.subheader("Отметьте критерии, исходя из которых будет подсчитана зарплата")

a36 = 1 if st.checkbox('Вахта') else 0

if experience == 'Без опыта':
    if a36:
        a0 =   1 if st.checkbox(model_0_code_experience_is_vahta_sorted[0]) else 0
        a1 =   1 if st.checkbox(model_0_code_experience_is_vahta_sorted[1]) else 0
        a2 =   1 if st.checkbox(model_0_code_experience_is_vahta_sorted[2]) else 0
        a3 =   1 if st.checkbox(model_0_code_experience_is_vahta_sorted[3]) else 0
        a4 =   1 if st.checkbox(model_0_code_experience_is_vahta_sorted[4]) else 0
        a5 =   1 if st.checkbox(model_0_code_experience_is_vahta_sorted[5]) else 0
        a6 =   1 if st.checkbox(model_0_code_experience_is_vahta_sorted[6]) else 0
        a7 =   1 if st.checkbox(model_0_code_experience_is_vahta_sorted[7]) else 0
        a8 =   1 if st.checkbox(model_0_code_experience_is_vahta_sorted[8]) else 0
        a9 =   1 if st.checkbox(model_0_code_experience_is_vahta_sorted[9]) else 0
        a10 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[10]) else 0
        a11 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[11]) else 0
        a12 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[12]) else 0
        a13 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[13]) else 0
        a14 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[14]) else 0
        a15 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[23]) else 0
        a24 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[24]) else 0
        a25 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[25]) else 0
        a26 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[26]) else 0
        a27 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[27]) else 0
        a28 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[28]) else 0
        a29 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[29]) else 0
        a30 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[30]) else 0
        a31 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[31]) else 0
        a32 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[32]) else 0
        a33 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[33]) else 0
        a34 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[34]) else 0
        a35 = 1 if st.checkbox(model_0_code_experience_is_vahta_sorted[35]) else 0
        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35])[model_0_code_experience_is_vahta_sorted_mask]
        prediction = model_0_code_experience_is_vahta.predict(inputs)
    else:
        a0 =   1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[0]) else 0
        a1 =   1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[1]) else 0
        a2 =   1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[2]) else 0
        a3 =   1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[3]) else 0
        a4 =   1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[4]) else 0
        a5 =   1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[5]) else 0
        a6 =   1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[6]) else 0
        a7 =   1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[7]) else 0
        a8 =   1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[8]) else 0
        a9 =   1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[9]) else 0
        a10 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[10]) else 0
        a11 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[11]) else 0
        a12 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[12]) else 0
        a13 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[13]) else 0
        a14 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[14]) else 0
        a15 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[23]) else 0
        a24 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[24]) else 0
        a25 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[25]) else 0
        a26 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[26]) else 0
        a27 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[27]) else 0
        a28 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[28]) else 0
        a29 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[29]) else 0
        a30 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[30]) else 0
        a31 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[31]) else 0
        a32 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[32]) else 0
        a33 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[33]) else 0
        a34 = 1 if st.checkbox(model_0_code_experience_isnt_vahta_sorted[34]) else 0
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))
        a35 = data[str(option)]
        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35])[model_0_code_experience_isnt_vahta_sorted_mask]
        prediction = model_0_code_experience_isnt_vahta.predict(inputs)

elif experience == 'От 1 до 3 лет':
    if a36:
        a0 =   1 if st.checkbox(model_1_code_experience_is_vahta_sorted[0]) else 0
        a1 =   1 if st.checkbox(model_1_code_experience_is_vahta_sorted[1]) else 0
        a2 =   1 if st.checkbox(model_1_code_experience_is_vahta_sorted[2]) else 0
        a3 =   1 if st.checkbox(model_1_code_experience_is_vahta_sorted[3]) else 0
        a4 =   1 if st.checkbox(model_1_code_experience_is_vahta_sorted[4]) else 0
        a5 =   1 if st.checkbox(model_1_code_experience_is_vahta_sorted[5]) else 0
        a6 =   1 if st.checkbox(model_1_code_experience_is_vahta_sorted[6]) else 0
        a7 =   1 if st.checkbox(model_1_code_experience_is_vahta_sorted[7]) else 0
        a8 =   1 if st.checkbox(model_1_code_experience_is_vahta_sorted[8]) else 0
        a9 =   1 if st.checkbox(model_1_code_experience_is_vahta_sorted[9]) else 0
        a10 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[10]) else 0
        a11 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[11]) else 0
        a12 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[12]) else 0
        a13 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[13]) else 0
        a14 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[14]) else 0
        a15 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[23]) else 0
        a24 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[24]) else 0
        a25 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[25]) else 0
        a26 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[26]) else 0
        a27 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[27]) else 0
        a28 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[28]) else 0
        a29 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[29]) else 0
        a30 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[30]) else 0
        a31 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[31]) else 0
        a32 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[32]) else 0
        a33 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[33]) else 0
        a34 = 1 if st.checkbox(model_1_code_experience_is_vahta_sorted[34]) else 0
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))
        a35 = data[str(option)]
        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35])[model_1_code_experience_is_vahta_sorted_mask]
        prediction = model_1_code_experience_is_vahta.predict(inputs)
    else:
        a0 =   1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[0]) else 0
        a1 =   1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[1]) else 0
        a2 =   1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[2]) else 0
        a3 =   1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[3]) else 0
        a4 =   1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[4]) else 0
        a5 =   1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[5]) else 0
        a6 =   1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[6]) else 0
        a7 =   1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[7]) else 0
        a8 =   1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[8]) else 0
        a9 =   1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[9]) else 0
        a10 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[10]) else 0
        a11 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[11]) else 0
        a12 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[12]) else 0
        a13 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[13]) else 0
        a14 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[14]) else 0
        a15 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[23]) else 0
        a24 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[24]) else 0
        a25 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[25]) else 0
        a26 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[26]) else 0
        a27 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[27]) else 0
        a28 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[28]) else 0
        a29 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[29]) else 0
        a30 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[30]) else 0
        a31 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[31]) else 0
        a32 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[32]) else 0
        a33 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[33]) else 0
        a34 = 1 if st.checkbox(model_1_code_experience_isnt_vahta_sorted[34]) else 0
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))
        a35 = data[str(option)]
        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35])[model_1_code_experience_isnt_vahta_sorted_mask]
        prediction = model_1_code_experience_isnt_vahta.predict(inputs)

else:
    if a36:
        a0 =   1 if st.checkbox(model_2_code_experience_is_vahta_sorted[0]) else 0
        a1 =   1 if st.checkbox(model_2_code_experience_is_vahta_sorted[1]) else 0
        a2 =   1 if st.checkbox(model_2_code_experience_is_vahta_sorted[2]) else 0
        a3 =   1 if st.checkbox(model_2_code_experience_is_vahta_sorted[3]) else 0
        a4 =   1 if st.checkbox(model_2_code_experience_is_vahta_sorted[4]) else 0
        a5 =   1 if st.checkbox(model_2_code_experience_is_vahta_sorted[5]) else 0
        a6 =   1 if st.checkbox(model_2_code_experience_is_vahta_sorted[6]) else 0
        a7 =   1 if st.checkbox(model_2_code_experience_is_vahta_sorted[7]) else 0
        a8 =   1 if st.checkbox(model_2_code_experience_is_vahta_sorted[8]) else 0
        a9 =   1 if st.checkbox(model_2_code_experience_is_vahta_sorted[9]) else 0
        a10 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[10]) else 0
        a11 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[11]) else 0
        a12 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[12]) else 0
        a13 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[13]) else 0
        a14 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[14]) else 0
        a15 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[23]) else 0
        a24 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[24]) else 0
        a25 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[25]) else 0
        a26 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[26]) else 0
        a27 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[27]) else 0
        a28 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[28]) else 0
        a29 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[29]) else 0
        a30 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[30]) else 0
        a31 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[31]) else 0
        a32 = 1 if st.checkbox(model_2_code_experience_is_vahta_sorted[32]) else 0
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))
        a33 = data[str(option)]
        
        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33])[model_1_code_experience_is_vahta_sorted_mask]
        prediction = model_2_code_experience_is_vahta.predict(inputs)
    else:
        a0 =   1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[0]) else 0
        a1 =   1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[1]) else 0
        a2 =   1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[2]) else 0
        a3 =   1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[3]) else 0
        a4 =   1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[4]) else 0
        a5 =   1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[5]) else 0
        a6 =   1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[6]) else 0
        a7 =   1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[7]) else 0
        a8 =   1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[8]) else 0
        a9 =   1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[9]) else 0
        a10 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[10]) else 0
        a11 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[11]) else 0
        a12 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[12]) else 0
        a13 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[13]) else 0
        a14 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[14]) else 0
        a15 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[23]) else 0
        a24 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[24]) else 0
        a25 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[25]) else 0
        a26 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[26]) else 0
        a27 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[27]) else 0
        a28 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[28]) else 0
        a29 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[29]) else 0
        a30 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[30]) else 0
        a31 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[31]) else 0
        a32 = 1 if st.checkbox(model_2_code_experience_isnt_vahta_sorted[32]) else 0

        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))
        a33 = data[str(option)]

        
        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33])[model_1_code_experience_isnt_vahta_sorted_mask]
        prediction = model_2_code_experience_isnt_vahta.predict(inputs)


if st.button('Предсказать зарплату'):
    prediction = abs(prediction)
    if prediction < 10000:
        prediction += 28541.867543
        
    st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(prediction, -1),2))}  рублей")
    




    # inputs = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, a48, a49, a50, a51, a52,region_ , a53]
    
    # if experience == 'Без опыта':
    #     if a53:
    #         prediction = model_0_code_experience_is_vahta.predict(inputs)
    #     else:
    #         prediction = model_0_code_experience_isnt_vahta.predict(inputs)

    # if experience == 'От 1 до 3 лет':
    #     if a53:
    #         prediction = model_1_code_experience_is_vahta.predict(inputs)
    #     else:
    #         prediction = model_1_code_experience_isnt_vahta.predict(inputs)
    # if experience == 'От 3 лет':
    #     if a53:
    #         prediction = model_2_code_experience_is_vahta.predict(inputs)
    #     else:
    #         prediction = model_2_code_experience_isnt_vahta.predict(inputs)
    
    # prediction = abs(prediction)
    # if prediction < 10000:
    #     prediction += 28541.867543
        
    # st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(prediction, -1),2))}  рублей")
    
