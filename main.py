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
        np.unique(['медсестра','сварщик']))

if inp_species == 'медсестра':
    name = 'medsestra'
    model_0_code_experience_sorted = list(json.load(open(f'{name}/model_0_code_experience_{name}.json')).keys())
    model_1_code_experience_sorted = list(json.load(open(f'{name}/model_1_code_experience_{name}.json')).keys())
    model_2_code_experience_sorted = list(json.load(open(f'{name}/model_2_code_experience_{name}.json')).keys())
    model_0_code_experience_rmse = 9561.680
    model_1_code_experience_rmse = 11819.859
    model_2_code_experience_rmse = 11792.724
    base_skills_0 = [x.strip() for x in open(f'{name}/base_skills_0_{name}.txt', 'r') if len(x) > 3]
    base_skills_1 = [x.strip() for x in open(f'{name}/base_skills_1_{name}.txt', 'r') if len(x) > 3]
    base_skills_2 = [x.strip() for x in open(f'{name}/base_skills_2_{name}.txt', 'r') if len(x) > 3]
    model_0_code_experience = CatBoostRegressor()
    model_0_code_experience.load_model(f'{name}/model_0_code_experience_{name}')
    model_1_code_experience = CatBoostRegressor()
    model_1_code_experience.load_model(f'{name}/model_1_code_experience_{name}')
    model_2_code_experience = CatBoostRegressor()
    model_2_code_experience.load_model(f'{name}/model_2_code_experience_{name}')
    m_order = [x.strip() for x in open(f'{name}/order_{name}.txt')]
    model_0_code_experience_sorted_mask = [model_0_code_experience_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_1_code_experience_sorted_mask = [model_1_code_experience_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_2_code_experience_sorted_mask = [model_2_code_experience_sorted.index(m_order[i]) for i in range(len(m_order))]

    
    st.header(f"Оценка стоимости навыков {inp_species}")
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
        for number,skill in enumerate(base_skills_0[:-1]):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
    
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
        a15 = 1 if st.checkbox(model_0_code_experience_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_0_code_experience_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_0_code_experience_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_0_code_experience_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_0_code_experience_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_0_code_experience_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_0_code_experience_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_0_code_experience_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_0_code_experience_sorted[23]) else 0

        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))

        a14 = data[str(option)]

        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22,a23])[model_0_code_experience_sorted_mask]
        prediction = model_0_code_experience.predict(inputs)
    

    elif experience == 'От 1 до 3 лет':
        st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
        for number,skill in enumerate(base_skills_1[:-1]):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

    
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
        # a11 = 1 if st.checkbox(model_1_code_experience_sorted[11]) else 0
        a12 = 1 if st.checkbox(model_1_code_experience_sorted[12]) else 0
        a13 = 1 if st.checkbox(model_1_code_experience_sorted[13]) else 0
        a14 = 1 if st.checkbox(model_1_code_experience_sorted[14]) else 0
        a15 = 1 if st.checkbox(model_1_code_experience_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_1_code_experience_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_1_code_experience_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_1_code_experience_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_1_code_experience_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_1_code_experience_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_1_code_experience_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_1_code_experience_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_1_code_experience_sorted[23]) else 0
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))

        a11 = data[str(option)]

        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22,a23])[model_1_code_experience_sorted_mask]
        prediction = model_1_code_experience.predict(inputs)


    else:
        st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
        for number,skill in enumerate(base_skills_2[:-1]):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

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
        # a15 = 1 if st.checkbox(model_2_code_experience_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_2_code_experience_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_2_code_experience_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_2_code_experience_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_2_code_experience_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_2_code_experience_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_2_code_experience_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_2_code_experience_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_2_code_experience_sorted[23]) else 0
    
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))

        a15 = data[str(option)]

        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22,a23])[model_2_code_experience_sorted_mask]
        prediction = model_2_code_experience.predict(inputs)

        if prediction < 46000:
            prediction += 12932.31
            


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

        prices = json.load(open(f'{name}/model_0_code_experience_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = ['is_multiple' if 'рщик' in x else x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
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

        prices = json.load(open(f'{name}/model_1_code_experience_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = ['is_multiple' if 'рщик' in x else x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

    if flag == 2:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open(f'{name}/model_2_code_experience_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = ['is_multiple' if 'рщик' in x else x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

elif inp_species == 'сварщик':
    name = 'svarshik'
    model_0_code_experience_sorted = list(json.load(open(f'{name}/model_0_code_experience_{name}.json')).keys())
    model_1_code_experience_sorted = list(json.load(open(f'{name}/model_1_code_experience_{name}.json')).keys())
    model_2_code_experience_sorted = list(json.load(open(f'{name}/model_2_code_experience_{name}.json')).keys())
    model_0_code_experience_rmse = 33901.81
    model_1_code_experience_rmse = 33491.44
    model_2_code_experience_rmse = 35683.95
    base_skills_0 = [x.strip() for x in open(f'{name}/base_skills_0_{name}.txt', 'r') if len(x) > 3]
    base_skills_1 = [x.strip() for x in open(f'{name}/base_skills_1_{name}.txt', 'r') if len(x) > 3]
    base_skills_2 = [x.strip() for x in open(f'{name}/base_skills_2_{name}.txt', 'r') if len(x) > 3]
    model_0_code_experience = CatBoostRegressor()
    model_0_code_experience.load_model(f'{name}/model_0_code_experience_{name}')
    model_1_code_experience = CatBoostRegressor()
    model_1_code_experience.load_model(f'{name}/model_1_code_experience_{name}')
    model_2_code_experience = CatBoostRegressor()
    model_2_code_experience.load_model(f'{name}/model_2_code_experience_{name}')
    m_order = [x.strip() for x in open(f'{name}/order_{name}.txt')]
    model_0_code_experience_sorted_mask = [model_0_code_experience_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_1_code_experience_sorted_mask = [model_1_code_experience_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_2_code_experience_sorted_mask = [model_2_code_experience_sorted.index(m_order[i]) for i in range(len(m_order))]

    
    st.header(f"Оценка стоимости навыков {inp_species}")
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
        for number,skill in enumerate(base_skills_0[:-1]):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
    
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
        a20 = 1 if st.checkbox(model_0_code_experience_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_0_code_experience_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_0_code_experience_sorted[22]) else 0
        a23 = 1 if st.checkbox(model_0_code_experience_sorted[23]) else 0
        a24 = 1 if st.checkbox(model_0_code_experience_sorted[24]) else 0
        # a25 = 1 if st.checkbox(model_0_code_experience_sorted[23]) else 0

        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))

        a25 = data[str(option)]

        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22,a23,a24,a25])[model_0_code_experience_sorted_mask]
        prediction = model_0_code_experience.predict(inputs)
    

    elif experience == 'От 1 до 3 лет':
        st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
        for number,skill in enumerate(base_skills_1[:-1]):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

    
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
        a15 = 1 if st.checkbox(model_1_code_experience_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_1_code_experience_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_1_code_experience_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_1_code_experience_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_1_code_experience_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_1_code_experience_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_1_code_experience_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_1_code_experience_sorted[22]) else 0
        

        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))

        a25 = data[str(option)]

        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22,a23,a24,a25,a26])[model_1_code_experience_sorted_mask]
        prediction = model_1_code_experience.predict(inputs)


    else:
        st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
        for number,skill in enumerate(base_skills_2[:-1]):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

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
        a15 = 1 if st.checkbox(model_2_code_experience_sorted[15]) else 0
        a16 = 1 if st.checkbox(model_2_code_experience_sorted[16]) else 0
        a17 = 1 if st.checkbox(model_2_code_experience_sorted[17]) else 0
        a18 = 1 if st.checkbox(model_2_code_experience_sorted[18]) else 0
        a19 = 1 if st.checkbox(model_2_code_experience_sorted[19]) else 0
        a20 = 1 if st.checkbox(model_2_code_experience_sorted[20]) else 0
        a21 = 1 if st.checkbox(model_2_code_experience_sorted[21]) else 0
        a22 = 1 if st.checkbox(model_2_code_experience_sorted[22]) else 0

        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            (list(data.keys())))

        a25 = data[str(option)]

        inputs = np.array([a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22,a23,a24,a25,a26])[model_2_code_experience_sorted_mask]
        prediction = model_2_code_experience.predict(inputs)

        if prediction < 45000:
            prediction += 12932.31
            


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

        prices = json.load(open(f'{name}/model_0_code_experience_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = ['is_multiple' if 'рщик' in x else x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
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

        prices = json.load(open(f'{name}/model_1_code_experience_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = ['is_multiple' if 'рщик' in x else x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

    if flag == 2:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open(f'{name}/model_2_code_experience_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = ['is_multiple' if 'рщик' in x else x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
        