import streamlit as st
from catboost_install import install
try:
    from catboost import CatBoostRegressor
except:

    install('catboost')
    from catboost import CatBoostRegressor
import numpy as np
import json
import plotly.express as px
import pandas as pd



st.subheader("Выберите класс вакансии")
left_column, right_column = st.columns(2)
with left_column:
    inp_species = st.radio(
        'Наименование вакансии',
        np.unique(['Сварщик','Специалист по персоналу']))

if inp_species == 'Сварщик':



    base_skills_1 = ['Дополнительные льготы','Сварка без конкретизации вида/оборудования','Дуговая сварка','Удостоверения','Ручная сварка']
    base_skills_2 = ['НАКС','Требования к образованию','Дополнительные льготы','Сварка без конкретизации вида/оборудования','Дуговая сварка','Удостоверения','Ручная сварка',]
    m2_order = ['Сварка в среде аргона (РАД)\u200b', 'Обязательная сертификация', 'Обучение/профподготовка в компании', 'Плазменная сварка', 'Плазменная резка', 'Знания предметных областей для сварщика', 'Сборка и монтаж', 'Знание документации, проектов, чертежей, схем', 'Наплавка', 'Газовая сварка', 'Сварка в среде защитного газа', 'Знание правил безопасности', 'Знание техник, технологии сварки, наплавки', 'Газовая резка', 'Дуговая резка', 'Знание  устройств и правил эксплуатации сварочных аппаратов, машин', 'Настройка сварочного оборудования', 'Строгание', 'Строжка', 'Ручная резка', 'Бензо- и керосино- резание', 'Механизированная сварка', 'Автоматическая сварка', 'Резка', 'Обслуживание и ремонт сварочного оборудования', 'Действия перед/после сварки, резки', 'Контактная сварка', 'Чтение чертежей, документации', 'Соблюдение охраны труда, техники безопасности и пожарной безопасности', 'Контроль  сварки/резки, измерение', 'Пайка', 'Простые и средней сложности инструменты (изготовление, регулировка и ремонт)', 'Изготовление, регулировка и регулировка (простые узлы и средней сложности механизмы)', 'region_name_cat']
    m01_order = ['Сварка в среде аргона (РАД)\u200b', 'НАКС', 'Обязательная сертификация', 'Обучение/профподготовка в компании', 'Требования к образованию', 'Плазменная сварка', 'Плазменная резка', 'Знания предметных областей для сварщика', 'Сборка и монтаж', 'Знание документации, проектов, чертежей, схем', 'Наплавка', 'Газовая сварка', 'Сварка в среде защитного газа', 'Знание правил безопасности', 'Знание техник, технологии сварки, наплавки', 'Газовая резка', 'Дуговая резка', 'Знание  устройств и правил эксплуатации сварочных аппаратов, машин', 'Настройка сварочного оборудования', 'Строгание', 'Строжка', 'Ручная резка', 'Бензо- и керосино- резание', 'Механизированная сварка', 'Автоматическая сварка', 'Резка', 'Обслуживание и ремонт сварочного оборудования', 'Действия перед/после сварки, резки', 'Контактная сварка', 'Чтение чертежей, документации', 'Соблюдение охраны труда, техники безопасности и пожарной безопасности', 'Контроль  сварки/резки, измерение', 'Пайка', 'Простые и средней сложности инструменты (изготовление, регулировка и ремонт)', 'Изготовление, регулировка и регулировка (простые узлы и средней сложности механизмы)', 'region_name_cat']


    model_0_code_experience_is_vahta_sorted = list(json.load(open('model_0_code_experience_is_vahta_sorted.json')).keys()) +['region_name_cat']
    model_1_code_experience_is_vahta_sorted = list(json.load(open('model_1_code_experience_is_vahta_sorted.json')).keys())+['region_name_cat']
    model_2_code_experience_is_vahta_sorted = list(json.load(open('model_2_code_experience_is_vahta_sorted.json')).keys())+['region_name_cat']
    model_0_code_experience_isnt_vahta_sorted = list(json.load(open('model_0_code_experience_isnt_vahta_sorted.json')).keys())+['region_name_cat']
    model_1_code_experience_isnt_vahta_sorted = list(json.load(open('model_1_code_experience_isnt_vahta_sorted.json')).keys())+['region_name_cat']
    model_2_code_experience_isnt_vahta_sorted = list(json.load(open('model_2_code_experience_isnt_vahta_sorted.json')).keys())+['region_name_cat']


    model_0_code_experience_is_vahta_sorted_mask = [model_0_code_experience_is_vahta_sorted.index(m01_order[i]) for i in range(36)]
    model_0_code_experience_isnt_vahta_sorted_mask = [model_0_code_experience_isnt_vahta_sorted.index(m01_order[i]) for i in range(36)]
    model_1_code_experience_is_vahta_sorted_mask = [model_1_code_experience_is_vahta_sorted.index(m01_order[i]) for i in range(36)]
    model_1_code_experience_isnt_vahta_sorted_mask = [model_1_code_experience_isnt_vahta_sorted.index(m01_order[i]) for i in range(36)]
    model_2_code_experience_is_vahta_sorted_mask = [model_2_code_experience_is_vahta_sorted.index(m2_order[i]) for i in range(34)]
    model_2_code_experience_isnt_vahta_sorted_mask = [model_2_code_experience_isnt_vahta_sorted.index(m2_order[i]) for i in range(34)]

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



    flag = -1




    st.subheader("Выберите стаж работы")
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        experience = st.radio(
            'опыт работы:',
            np.unique(['Без опыта', 'От 1 до 3 лет','От 3 лет']))

    f = open('regions_final.json')
    data = json.load(f)


    a36 = 1 if st.checkbox('Вахта') else 0

    if experience == 'Без опыта':
        st.subheader("Базовые навыки Сварщик Без опыта:")
        for number,skill in enumerate(base_skills_1):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания стоимости (см. развернутый график внизу страницы)")
    
        if a36:
            flag = 0
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
            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                (list(data.keys())))
            a35 = data[str(option)]

            inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35])[model_0_code_experience_is_vahta_sorted_mask]
            prediction = model_0_code_experience_is_vahta.predict(inputs)


        else:
            flag = 1
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
        st.subheader("Базовые навыки Сварщик От 1 до 3 лет:")
        for number,skill in enumerate(base_skills_1):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания стоимости (см. развернутый график внизу страницы)")

    
        if a36:
            flag = 2
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
            flag = 3
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
        st.subheader("Базовые навыки Сварщик Более 3 лет опыта:")
        for number,skill in enumerate(base_skills_2):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания стоимости (см. развернутый график внизу страницы)")

        if a36:
            flag = 4
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
            
            inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33])[model_2_code_experience_is_vahta_sorted_mask]
            prediction = model_2_code_experience_is_vahta.predict(inputs)

        else:
            flag = 5
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

            
            inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33])[model_2_code_experience_isnt_vahta_sorted_mask]
            prediction = model_2_code_experience_isnt_vahta.predict(inputs)
            
            

    model_0_code_experience_is_vahta_rmse = 24309.1451
    model_0_code_experience_isnt_vahta_rmse = 18835.0906
    model_1_code_experience_is_vahta_rmse = 21428.43
    model_1_code_experience_isnt_vahta_rmse = 27549.1031
    model_2_code_experience_is_vahta_rmse = 24441.3256
    model_2_code_experience_isnt_vahta_rmse = 22959.09548

    if st.button('Предсказать зарплату'):
        pr = abs(prediction)
        if pr < 10000: pr += 23914.49832
        if flag == 0:
            p1 = pr - model_0_code_experience_is_vahta_rmse/2
            p2 = pr +model_0_code_experience_is_vahta_rmse/2
        
        if flag == 1:
            p1 = pr - model_0_code_experience_isnt_vahta_rmse/2
            p2 = pr +model_0_code_experience_isnt_vahta_rmse/2
        
        if flag == 2:
            p1 = pr - model_1_code_experience_is_vahta_rmse/2
            p2 = pr +model_1_code_experience_is_vahta_rmse/2
        
        if flag == 3:
            p1 = pr - model_1_code_experience_isnt_vahta_rmse/2
            p2 = pr +model_1_code_experience_isnt_vahta_rmse/2

        if flag == 4:
            p1 = pr - model_2_code_experience_is_vahta_rmse/2
            p2 = pr +model_2_code_experience_is_vahta_rmse/2
        
        if flag == 5:
            p1 = pr - model_2_code_experience_isnt_vahta_rmse/2
            p2 = pr + model_2_code_experience_isnt_vahta_rmse/2
        
        st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(p1, -1),2))} - {'{:.2f}'.format(round(np.squeeze(p2, -1),2))} рублей")


    if flag == 0:
        st.subheader("")
        st.subheader("")
        st.subheader("Гистограмма стоимости навыков Сварщик Без опыта Вахта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

        prices = json.load(open('model_0_code_experience_is_vahta_sorted.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = prices.keys(),columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Стоимость', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")
        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)


    if flag == 1:
        st.subheader("")
        st.subheader("")
        st.subheader("Гистограмма стоимости навыков Сварщик Без опыта Не вахта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

        prices = json.load(open('model_0_code_experience_isnt_vahta_sorted.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = prices.keys(),columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Стоимость', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")
        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

    if flag == 2:
        st.subheader("")
        st.subheader("")
        st.subheader("Гистограмма стоимости навыков Сварщик От 1 до 3 лет опыта Вахта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

        prices = json.load(open('model_1_code_experience_is_vahta_sorted.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = prices.keys(),columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Стоимость', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

    if flag == 3:
        st.subheader("")
        st.subheader("")
        st.subheader("Гистограмма стоимости навыков Сварщик От 1 до 3 лет опыта Не Вахта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

        prices = json.load(open('model_1_code_experience_isnt_vahta_sorted.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = prices.keys(),columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Стоимость', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

    if flag == 4:
        st.subheader("")
        st.subheader("")
        st.subheader("Гистограмма стоимости навыков Сварщик Более 3 лет опыта Вахта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open('model_2_code_experience_is_vahta_sorted.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = prices.keys(),columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Стоимость', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

    if flag == 5:
        st.subheader("")
        st.subheader("")
        st.subheader("Гистограмма стоимости навыков Сварщик Более 3 лет опыта Не Вахта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

        prices = json.load(open('model_2_code_experience_isnt_vahta_sorted.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = prices.keys(),columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Стоимость', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

            
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
else:

    model_0_code_experience_sorted = list(json.load(open('model_0_code_experience.json')).keys())
    model_1_code_experience_sorted = list(json.load(open('model_1_code_experience.json')).keys())
    model_2_code_experience_sorted = list(json.load(open('model_2_code_experience_hr.json')).keys())
    model_0_code_experience_rmse = 13622.6
    model_1_code_experience_rmse = 14896.5
    model_2_code_experience_rmse = 17330
    base_skills_0 = ['Требования к образованию', 'Зарплата и другие выплаты, официальное трудоустройство', 'График работы', 'Личные установки и ценности, мировоззрение', 'Карьера', 'Условия работы/проживания/отдыха', 'Административные функции', 'Поиск и подбор персонала (СУП)', 'Развитие персонала (СУП)', 'Организация и оплата труда персонала СУП)', 'Обеспечение корпоративной и социальной политики (СУП)', 'Требование к опыту работы и образованию (СУП)', 'Не соответствует СУП']
    base_skills_1 = ['Требования к образованию', 'Зарплата и другие выплаты, официальное трудоустройство', 'График работы', 'Личные установки и ценности, мировоззрение', 'Карьера', 'Условия работы/проживания/отдыха', 'Административные функции', 'Поиск и подбор персонала (СУП)', 'Оценка и аттестация персонала (СУП)', 'Развитие персонала (СУП)', 'Организация и оплата труда персонала СУП)', 'Обеспечение корпоративной и социальной политики (СУП)', 'Требование к опыту работы и образованию (СУП)', 'Не соответствует СУП']
    base_skills_2 = ['Требования к образованию', 'Зарплата и другие выплаты, официальное трудоустройство', 'График работы', 'Личные установки и ценности, мировоззрение', 'Карьера', 'Условия работы/проживания/отдыха', 'Административные функции', 'Поиск и подбор персонала (СУП)', 'Оценка и аттестация персонала (СУП)', 'Развитие персонала (СУП)', 'Организация и оплата труда персонала СУП)', 'Обеспечение корпоративной и социальной политики (СУП)', 'Требование к опыту работы и образованию (СУП)', 'Не соответствует СУП']
    model_0_code_experience = CatBoostRegressor()
    model_0_code_experience.load_model('model_0_code_experience_hr')
    model_1_code_experience = CatBoostRegressor()
    model_1_code_experience.load_model('model_1_code_experience_hr')
    model_2_code_experience = CatBoostRegressor()
    model_2_code_experience.load_model('model_2_code_experience_hr')
    m_order = ['is_distance', 'is_parttime', 'v3_region_index', 'Работа в 1С', 'Английский язык', 'Опыт работы', 'Опыт работы не обязателен', 'Обучение/профподготовка в компании', 'Требования к образованию', 'Дополнительные льготы', 'Зарплата и другие выплаты, официальное трудоустройство', 'График работы', 'Русский язык', 'Личные установки и ценности, мировоззрение', 'Знания предметных областей для сварщика', 'Карьера', 'Условия работы/проживания/отдыха', 'Административные функции', 'Специальное ПО', 'Поиск и подбор персонала (СУП)', 'Кадровое делопроизводство (СУП)', 'Знания в области поиска и подбора персонала (СУП)', 'Оценка и аттестация персонала (СУП)', 'Знания в области оценки и аттестации персонала (СУП)', 'Развитие персонала (СУП)', 'Организация и оплата труда персонала СУП)', 'Обеспечение корпоративной и социальной политики (СУП)', 'Требование к опыту работы и образованию (СУП)', 'Ведение медицинской документации', 'Не соответствует СУП', 'Компьютерные программы для ведения бухгалтерского учета', 'Оформление учетно-отчетной документации', 'Пользоваться компьютерными и телекоммуникационными средствами в профессиональной деятельности']
    model_0_code_experience_sorted_mask = [model_0_code_experience_sorted.index(m_order[i]) for i in range(33)]
    model_1_code_experience_sorted_mask = [model_1_code_experience_sorted.index(m_order[i]) for i in range(33)]
    model_2_code_experience_sorted_mask = [model_2_code_experience_sorted.index(m_order[i]) for i in range(33)]

    
    st.header("Предсказание зарплаты по вакансии сварщика исходя из навыков")
    # data = pd.read_csv("fish.csv")

    st.subheader("Выберите стаж работы")
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        experience = st.radio(
            'опыт работы:',
            np.unique(['Без опыта', 'От 1 до 3 лет','От 3 лет']))

    f = open('regions_final.json')
    data = json.load(f)



    if experience == 'Без опыта':
        st.subheader(f"Базовые навыки {inp_species} Без опыта:")
        for number,skill in enumerate(base_skills_0):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания стоимости (см. развернутый график внизу страницы)")
    
        flag = 0
        a0 =   1 if st.checkbox(model_0_code_experience_sorted[0]) else 0
        a1 =   1 if st.checkbox(model_0_code_experience_sorted[1]) else 0
        a2 =   1 if st.checkbox(model_0_code_experience_sorted[2]) else 0
        a3 =   1 if st.checkbox(model_0_code_experience_sorted[3]) else 0
        a4 =   1 if st.checkbox(model_0_code_experience_sorted[4]) else 0
        a5 =   1 if st.checkbox(model_0_code_experience_sorted[5]) else 0
        a6 =   1 if st.checkbox(model_0_code_experience_sorted[6]) else 0
        a7 =   1 if st.checkbox(model_0_code_experience_sorted[7]) else 0
        a8 =   1 if st.checkbox(model_0_code_experience_sorted[8]) else 0
        a9 =   1 if st.checkbox(model_0_code_experience_sorted[9]) else 0
        a10 = 1 if st.checkbox(model_0_code_experience_sorted[10]) else 0
        a11 = 1 if st.checkbox(model_0_code_experience_sorted[11]) else 0
        a12 = 1 if st.checkbox(model_0_code_experience_sorted[12]) else 0
        a13 = 1 if st.checkbox(model_0_code_experience_sorted[13]) else 0
        a14 = 1 if st.checkbox(model_0_code_experience_sorted[14]) else 0
        a15 = 1 if st.checkbox(model_0_code_experience_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_0_code_experience_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_0_code_experience_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_0_code_experience_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_0_code_experience_sorted[19]) else 0
        # a20 = 1 if st.checkbox(model_0_code_experience_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_0_code_experience_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_0_code_experience_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_0_code_experience_sorted[23]) else 0
        a24 = 1 if st.checkbox(model_0_code_experience_sorted[24]) else 0
        a25 = 1 if st.checkbox(model_0_code_experience_sorted[25]) else 0
        a26 = 1 if st.checkbox(model_0_code_experience_sorted[26]) else 0
        a27 = 1 if st.checkbox(model_0_code_experience_sorted[27]) else 0
        a28 = 1 if st.checkbox(model_0_code_experience_sorted[28]) else 0
        a29 = 1 if st.checkbox(model_0_code_experience_sorted[29]) else 0
        a30 = 1 if st.checkbox(model_0_code_experience_sorted[30]) else 0
        a31 = 1 if st.checkbox(model_0_code_experience_sorted[31]) else 0

    
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))
        a20 = data[str(option)]
        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31])[model_0_code_experience_sorted_mask]
        prediction = model_0_code_experience.predict(inputs)
    

    elif experience == 'От 1 до 3 лет':
        st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
        for number,skill in enumerate(base_skills_1):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания стоимости (см. развернутый график внизу страницы)")

    
        flag = 1
        a0 =   1 if st.checkbox(model_1_code_experience_sorted[0]) else 0
        a1 =   1 if st.checkbox(model_1_code_experience_sorted[1]) else 0
        a2 =   1 if st.checkbox(model_1_code_experience_sorted[2]) else 0
        a3 =   1 if st.checkbox(model_1_code_experience_sorted[3]) else 0
        a4 =   1 if st.checkbox(model_1_code_experience_sorted[4]) else 0
        a5 =   1 if st.checkbox(model_1_code_experience_sorted[5]) else 0
        a6 =   1 if st.checkbox(model_1_code_experience_sorted[6]) else 0
        a7 =   1 if st.checkbox(model_1_code_experience_sorted[7]) else 0
        a8 =   1 if st.checkbox(model_1_code_experience_sorted[8]) else 0
        a9 =   1 if st.checkbox(model_1_code_experience_sorted[9]) else 0
        a10 = 1 if st.checkbox(model_1_code_experience_sorted[10]) else 0
        a11 = 1 if st.checkbox(model_1_code_experience_sorted[11]) else 0
        a12 = 1 if st.checkbox(model_1_code_experience_sorted[12]) else 0
        a13 = 1 if st.checkbox(model_1_code_experience_sorted[13]) else 0
        a14 = 1 if st.checkbox(model_1_code_experience_sorted[14]) else 0
        a15 = 1 if st.checkbox(model_1_code_experience_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_1_code_experience_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_1_code_experience_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_1_code_experience_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_1_code_experience_sorted[19]) else 0
        # a20 = 1 if st.checkbox(model_1_code_experience_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_1_code_experience_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_1_code_experience_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_1_code_experience_sorted[23]) else 0
        a24 = 1 if st.checkbox(model_1_code_experience_sorted[24]) else 0
        a25 = 1 if st.checkbox(model_1_code_experience_sorted[25]) else 0
        a26 = 1 if st.checkbox(model_1_code_experience_sorted[26]) else 0
        a27 = 1 if st.checkbox(model_1_code_experience_sorted[27]) else 0
        a28 = 1 if st.checkbox(model_1_code_experience_sorted[28]) else 0
        a29 = 1 if st.checkbox(model_1_code_experience_sorted[29]) else 0
        a30 = 1 if st.checkbox(model_1_code_experience_sorted[30]) else 0
        a31 = 1 if st.checkbox(model_1_code_experience_sorted[31]) else 0

    
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))
        a20 = data[str(option)]
        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31])[model_1_code_experience_sorted_mask]
        prediction = model_1_code_experience.predict(inputs)


    else:
        st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
        for number,skill in enumerate(base_skills_2):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания стоимости (см. развернутый график внизу страницы)")

        flag = 2
        a0 =   1 if st.checkbox(model_2_code_experience_sorted[0]) else 0
        a1 =   1 if st.checkbox(model_2_code_experience_sorted[1]) else 0
        a2 =   1 if st.checkbox(model_2_code_experience_sorted[2]) else 0
        a3 =   1 if st.checkbox(model_2_code_experience_sorted[3]) else 0
        a4 =   1 if st.checkbox(model_2_code_experience_sorted[4]) else 0
        a5 =   1 if st.checkbox(model_2_code_experience_sorted[5]) else 0
        a6 =   1 if st.checkbox(model_2_code_experience_sorted[6]) else 0
        a7 =   1 if st.checkbox(model_2_code_experience_sorted[7]) else 0
        a8 =   1 if st.checkbox(model_2_code_experience_sorted[8]) else 0
        a9 =   1 if st.checkbox(model_2_code_experience_sorted[9]) else 0
        a10 = 1 if st.checkbox(model_2_code_experience_sorted[10]) else 0
        a11 = 1 if st.checkbox(model_2_code_experience_sorted[11]) else 0
        a12 = 1 if st.checkbox(model_2_code_experience_sorted[12]) else 0
        a13 = 1 if st.checkbox(model_2_code_experience_sorted[13]) else 0
        a14 = 1 if st.checkbox(model_2_code_experience_sorted[14]) else 0
        a15 = 1 if st.checkbox(model_2_code_experience_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_2_code_experience_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_2_code_experience_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_2_code_experience_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_2_code_experience_sorted[19]) else 0
        # a20 = 1 if st.checkbox(model_2_code_experience_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_2_code_experience_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_2_code_experience_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_2_code_experience_sorted[23]) else 0
        a24 = 1 if st.checkbox(model_2_code_experience_sorted[24]) else 0
        a25 = 1 if st.checkbox(model_2_code_experience_sorted[25]) else 0
        a26 = 1 if st.checkbox(model_2_code_experience_sorted[26]) else 0
        a27 = 1 if st.checkbox(model_2_code_experience_sorted[27]) else 0
        a28 = 1 if st.checkbox(model_2_code_experience_sorted[28]) else 0
        a29 = 1 if st.checkbox(model_2_code_experience_sorted[29]) else 0
        a30 = 1 if st.checkbox(model_2_code_experience_sorted[30]) else 0
        a31 = 1 if st.checkbox(model_2_code_experience_sorted[31]) else 0

    
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))
        a20 = data[str(option)]
        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31])[model_2_code_experience_sorted_mask]
        prediction = model_2_code_experience.predict(inputs)    
            


    if st.button('Предсказать зарплату'):
        pr = abs(prediction)
        if pr < 10000: pr += 13041.49832
        if flag == 0:
            p1 = pr - model_0_code_experience_rmse/2
            p2 = pr +model_0_code_experience_rmse/2
        
        if flag == 1:
            p1 = pr - model_1_code_experience_rmse/2
            p2 = pr +model_1_code_experience_rmse/2
        
        if flag == 2:
            p1 = pr - model_2_code_experience_rmse/2
            p2 = pr +model_2_code_experience_rmse/2
        
        
        st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(p1, -1),2))} - {'{:.2f}'.format(round(np.squeeze(p2, -1),2))} рублей")


    if flag == 0:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Без опытa")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

        prices = json.load(open('model_0_code_experience_sorted.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = prices.keys(),columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Стоимость', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")
        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)


    
    if flag == 1:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} От 1 до 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

        prices = json.load(open('model_1_code_experience_sorted.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = prices.keys(),columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Стоимость', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

    if flag == 4:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта Вахта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open('model_2_code_experience_sorted.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = prices.keys(),columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Стоимость', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
        
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
    