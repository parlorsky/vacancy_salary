import streamlit as st
from catboost import CatBoostRegressor
import numpy as np
import json



cols = [
    'НАКС',
    'Развитие персонала (СУП)',
 'Разборка, ремонт, сборка, регулирование и испытание простых и средней сложности узлов, механизмов, оборудования',
 'Сварка трением',
 'Экструзионная сварка',
 'Разборка, ремонт, сборка, испытание и наладка сложных узлов, механизмов, оборудования',
 'Врезка в трубопроводы',
 'Пользоваться компьютерными и телекоммуникационными средствами в профессиональной деятельности',
 'Сварка нагретым инструментом',
 'Изготовление, регулировка и регулировка (простые узлы и средней сложности механизмы)',
 'Ремонт сварочных аппаратов, машин',
 'Сложные, точные инструменты (изготовление, регулировка и ремонт)',
 'Английский язык',
 'Бензо- и керосино- резание',
 'Строгание',
 'Обслуживание и ремонт сварочного оборудования',
 'Дуговая резка',
 'Резка',
 'Простые и средней сложности инструменты (изготовление, регулировка и ремонт)',
 'Знания предметных областей для сварщика',
 'Отсутствие требований по сертификации',
 'Строжка',
 'Настройка сварочного оборудования',
 'Плазменная резка',
 'Контактная сварка',
 'Специальное ПО',
 'Действия перед/после сварки, резки',
 'Газовая резка',
 'Ручная резка',
 'Знание  устройств и правил эксплуатации сварочных аппаратов, машин',
 'Сборка и монтаж',
 'Соблюдение охраны труда, техники безопасности и пожарной безопасности',
 'Ручная сварка',
 'Контроль  сварки/резки, измерение',
 'Плазменная сварка',
 'Сварка в среде защитного газа',
 'Дуговая сварка',
 'Чтение чертежей, документации',
 'Знание техник, технологии сварки, наплавки',
 'Пайка',
 'Знание документации, проектов, чертежей, схем',
 'Наплавка',
 'Автоматическая сварка',
 'Механизированная сварка',
 'Сварка без конкретизации вида/оборудования',
 'Газовая сварка',
 'Обучение/профподготовка в компании',
 'Сварка в среде аргона (РАД)\u200b',
 'Знание правил безопасности',
 'Требования к образованию',
 'Удостоверения',
 'Обязательная сертификация',
 'Дополнительные льготы',
 'is_vahta']


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



st.subheader("Выберите тип вакансии")
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


a0 = 1 if st.checkbox(cols[0]) else 0
a1 = 1 if st.checkbox(cols[1]) else 0
a2 = 1 if st.checkbox(cols[2]) else 0
a3 = 1 if st.checkbox(cols[3]) else 0
a4 = 1 if st.checkbox(cols[4]) else 0
a5 = 1 if st.checkbox(cols[5]) else 0
a6 = 1 if st.checkbox(cols[6]) else 0
a7 = 1 if st.checkbox(cols[7]) else 0
a8 = 1 if st.checkbox(cols[8]) else 0
a9 = 1 if st.checkbox(cols[9]) else 0
a10 = 1 if st.checkbox(cols[10]) else 0
a11 = 1 if st.checkbox(cols[11]) else 0
a12 = 1 if st.checkbox(cols[12]) else 0
a13 = 1 if st.checkbox(cols[13]) else 0
a14 = 1 if st.checkbox(cols[14]) else 0
a15 = 1 if st.checkbox(cols[15]) else 0
a16 = 1 if st.checkbox(cols[16]) else 0
a17 = 1 if st.checkbox(cols[17]) else 0
a18 = 1 if st.checkbox(cols[18]) else 0
a19 = 1 if st.checkbox(cols[19]) else 0
a20 = 1 if st.checkbox(cols[20]) else 0
a21 = 1 if st.checkbox(cols[21]) else 0
a22 = 1 if st.checkbox(cols[22]) else 0
a23 = 1 if st.checkbox(cols[23]) else 0
a24 = 1 if st.checkbox(cols[24]) else 0
a25 = 1 if st.checkbox(cols[25]) else 0
a26 = 1 if st.checkbox(cols[26]) else 0
a27 = 1 if st.checkbox(cols[27]) else 0
a28 = 1 if st.checkbox(cols[28]) else 0
a29 = 1 if st.checkbox(cols[29]) else 0
a30 = 1 if st.checkbox(cols[30]) else 0
a31 = 1 if st.checkbox(cols[31]) else 0
a32 = 1 if st.checkbox(cols[32]) else 0
a33 = 1 if st.checkbox(cols[33]) else 0
a34 = 1 if st.checkbox(cols[34]) else 0
a35 = 1 if st.checkbox(cols[35]) else 0
a36 = 1 if st.checkbox(cols[36]) else 0
a37 = 1 if st.checkbox(cols[37]) else 0
a38 = 1 if st.checkbox(cols[38]) else 0
a39 = 1 if st.checkbox(cols[39]) else 0
a40 = 1 if st.checkbox(cols[40]) else 0
a41 = 1 if st.checkbox(cols[41]) else 0
a42 = 1 if st.checkbox(cols[42]) else 0
a43 = 1 if st.checkbox(cols[43]) else 0
a44 = 1 if st.checkbox(cols[44]) else 0
a45 = 1 if st.checkbox(cols[45]) else 0
a46 = 1 if st.checkbox(cols[46]) else 0
a47 = 1 if st.checkbox(cols[47]) else 0
a48 = 1 if st.checkbox(cols[48]) else 0
a49 = 1 if st.checkbox(cols[49]) else 0
a50 = 1 if st.checkbox(cols[50]) else 0
a51 = 1 if st.checkbox(cols[51]) else 0
a52 = 1 if st.checkbox(cols[52]) else 0
a53 = 1 if st.checkbox('Вахта') else 0



f = open('regions_final.json')
data = json.load(f)

option = st.selectbox(
    'Напишите регион вакансии',
    (list(data.keys())))
region_ = data[str(option)]

if st.button('Предсказать зарплату'):
    inputs = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, a41, a42, a43, a44, a45, a46, a47, a48, a49, a50, a51, a52,region_ , a53]
    
    if experience == 'Без опыта':
        if a53:
            prediction = model_0_code_experience_is_vahta.predict(inputs)
        else:
            prediction = model_0_code_experience_isnt_vahta.predict(inputs)

    if experience == 'От 1 до 3 лет':
        if a53:
            prediction = model_1_code_experience_is_vahta.predict(inputs)
        else:
            prediction = model_1_code_experience_isnt_vahta.predict(inputs)
    if experience == 'От 3 лет':
        if a53:
            prediction = model_2_code_experience_is_vahta.predict(inputs)
        else:
            prediction = model_2_code_experience_isnt_vahta.predict(inputs)
        
        
    st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(prediction, -1),2))}  рублей")
    
