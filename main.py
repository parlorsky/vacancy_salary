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


rus_regs = ['Архангельская область',
 'город федерального значения Севастополь',
 'Республика Башкортостан',
 'Костромская область',
 'Новгородская область',
 'Рязанская область',
 'Республика Коми',
 'Владимирская область',
 'Томская область',
 'Республика Калмыкия',
 'Россия',
 'Республика Крым',
 'Красноярский край',
 'Республика Карелия',
 'Саратовская область',
 'Вологодская область',
 'Волгоградская область',
 'Еврейская автономная область',
 'Забайкальский край',
 'Иркутская область',
 'Ульяновская область',
 'Московская область',
 'Оренбургская область',
 'Сахалинская область',
 'Орловская область',
 'Белгородская область',
 'Челябинская область',
 'Республика Татарстан',
 'Республика Саха (Якутия)',
 'Магаданская область',
 'Республика Хакасия',
 'Хабаровский край',
 'Ямало-Ненецкий автономный округ',
 'Чукотский автономный округ',
 'Новосибирская область',
 'Республика Бурятия',
 'Ивановская область',
 'Кабардино-Балкарская Республика',
 'Псковская область',
 'Амурская область',
 'Тамбовская область',
 'Курская область',
 'Ростовская область',
 'Республика Ингушетия',
 'Липецкая область',
 'Алтайский край',
 'Воронежская область',
 'Камчатский край',
 'Омская область',
 'Смоленская область',
 'Город федерального значения Санкт-Петербург',
 'Свердловская область',
 'Чувашская Республика',
 'Брянская область',
 'Республика Тыва',
 'Кировская область',
 'Ставропольский край',
 'Карачаево-Черкесская Республика',
 'Ленинградская область',
 'Нижегородская область',
 'Республика Северная Осетия',
 'Калининградская область',
 'Республика Мордовия',
 'Мурманская область',
 'Город федерального значения Москва',
 'Республика Марий Эл',
 'Удмуртская Республика',
 'Самарская область',
 'Республика Дагестан',
 'Кемеровская область',
 'Краснодарский край',
 'Приморский край',
 'Тюменская область',
 'Республика Алтай',
 'Пензенская область',
 'Ненецкий автономный округ',
 'Тульская область',
 'Ярославская область',
 'Ханты-Мансийский автономный округ — Югра',
 'Республика Адыгея',
 'иные территории, включая город и космодром Байконур',
 'Чеченская Республика',
 'Пермский край',
 'Астраханская область',
 'Тверская область',
 'Курганская область',
 'Калужская область']


st.subheader("Выберите класс вакансии")
left_column, right_column = st.columns(2)
with left_column:
    inp_species = st.radio(
        'Наименование вакансии',
        np.unique(['медсестра','сварщик','слесарь','специалист по персоналу','продавец','слесарь КИПиА','слесарь-ремонтник','Слесарь механосборочных работ (MCP)']))

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

    st.subheader("Выберите опыт работы")
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

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
    
        flag = 0
        inputs = [1 if i in base_skills_0 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_sorted if x != 'v3_region_index']]
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            ([x for x in list(data.keys()) if x in rus_regs]))

        reg = data[str(option)]
        inputs.insert(model_0_code_experience_sorted.index('v3_region_index'),reg)
        inputs = np.array(inputs)[model_0_code_experience_sorted_mask]
        
        prediction = model_0_code_experience.predict(inputs)
    

    elif experience == 'От 1 до 3 лет':
        st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
        for number,skill in enumerate(base_skills_1):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

    
        flag = 1
        inputs = [1 if i in base_skills_1 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_sorted if x != 'v3_region_index']]
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            ([x for x in list(data.keys()) if x in rus_regs]))

        reg = data[str(option)]
        inputs.insert(model_1_code_experience_sorted.index('v3_region_index'),reg)
        inputs = np.array(inputs)[model_1_code_experience_sorted_mask]
        
        prediction = model_1_code_experience.predict(inputs)


    else:
        st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
        for number,skill in enumerate(base_skills_2):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        flag = 2
        inputs = [1 if i in base_skills_2 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_sorted if x != 'v3_region_index']]
        
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            ([x for x in list(data.keys()) if x in rus_regs]))

        reg = data[str(option)]
        inputs.insert(model_2_code_experience_sorted.index('v3_region_index'),reg)
        inputs = np.array(inputs)[model_2_code_experience_sorted_mask]
        
        prediction = model_2_code_experience.predict(inputs)

        if prediction < 46000:
            prediction += 12932.31
            


    if st.button('Рассчитать зарплату'):
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
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
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
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
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
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

elif inp_species == 'сварщик':
    name = 'svarshik'
    model_0_code_experience_y_sorted = list(json.load(open(f'{name}/model_0_code_experience_y_{name}.json')).keys())
    model_1_code_experience_y_sorted = list(json.load(open(f'{name}/model_1_code_experience_y_{name}.json')).keys())
    model_2_code_experience_y_sorted = list(json.load(open(f'{name}/model_2_code_experience_y_{name}.json')).keys())
    model_0_code_experience_n_sorted = list(json.load(open(f'{name}/model_0_code_experience_n_{name}.json')).keys())
    model_1_code_experience_n_sorted = list(json.load(open(f'{name}/model_1_code_experience_n_{name}.json')).keys())
    model_2_code_experience_n_sorted = list(json.load(open(f'{name}/model_2_code_experience_n_{name}.json')).keys())
    
    model_0_code_experience_y_rmse = 21786.00
    model_1_code_experience_y_rmse = 24340.647
    model_2_code_experience_y_rmse = 24097.07
    model_0_code_experience_n_rmse = 11808.04
    model_1_code_experience_n_rmse = 18843.72
    model_2_code_experience_n_rmse = 20997.25

    base_skills_0 = [x.strip() for x in open(f'{name}/base_skills_0_{name}.txt', 'r') if len(x) > 3]
    base_skills_1 = [x.strip() for x in open(f'{name}/base_skills_1_{name}.txt', 'r') if len(x) > 3]
    base_skills_2 = [x.strip() for x in open(f'{name}/base_skills_2_{name}.txt', 'r') if len(x) > 3]
    
    model_0_code_experience_y = CatBoostRegressor()
    model_0_code_experience_y.load_model(f'{name}/model_0_code_experience_y_{name}')
    model_1_code_experience_y = CatBoostRegressor()
    model_1_code_experience_y.load_model(f'{name}/model_1_code_experience_y_{name}')
    model_2_code_experience_y = CatBoostRegressor()
    model_2_code_experience_y.load_model(f'{name}/model_2_code_experience_y_{name}')
    model_0_code_experience_n = CatBoostRegressor()
    model_0_code_experience_n.load_model(f'{name}/model_0_code_experience_n_{name}')
    model_1_code_experience_n = CatBoostRegressor()
    model_1_code_experience_n.load_model(f'{name}/model_1_code_experience_n_{name}')
    model_2_code_experience_n = CatBoostRegressor()
    model_2_code_experience_n.load_model(f'{name}/model_2_code_experience_n_{name}')

    m_order = [x.strip() for x in open(f'{name}/order_{name}.txt')]
    model_0_code_experience_y_sorted_mask = [model_0_code_experience_y_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_1_code_experience_y_sorted_mask = [model_1_code_experience_y_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_2_code_experience_y_sorted_mask = [model_2_code_experience_y_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_0_code_experience_n_sorted_mask = [model_0_code_experience_n_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_1_code_experience_n_sorted_mask = [model_1_code_experience_n_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_2_code_experience_n_sorted_mask = [model_2_code_experience_n_sorted.index(m_order[i]) for i in range(len(m_order))]

    
    st.header(f"Оценка стоимости навыков {inp_species}")
    # data = pd.read_csv("fish.csv")

    st.subheader("Выберите опыт работы")
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        experience = st.radio(
            'опыт работы:',
            np.unique(['Без опыта', 'От 1 до 3 лет','От 3 лет']))

    f = open('regions_final.json')
    data = json.load(f)

    vahta = 1 if st.checkbox('Вахта') else 0
    if vahta:
        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 0
            inputs = [1 if i in base_skills_0 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_y_sorted if x != 'v3_region_index']]
        
       
            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_0_code_experience_y_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_0_code_experience_y_sorted_mask]
            prediction = model_0_code_experience_y.predict(inputs)
            

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 1
            inputs = [1 if i in base_skills_1 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_y_sorted if x != 'v3_region_index']]
                

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))

            reg = data[str(option)]
            inputs.insert(model_1_code_experience_y_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_1_code_experience_y_sorted_mask]
            prediction = model_1_code_experience_y.predict(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 2
            inputs = [1 if i in base_skills_2 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_y_sorted if x != 'v3_region_index']]
            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))

            reg = data[str(option)]
            inputs.insert(model_2_code_experience_y_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_2_code_experience_y_sorted_mask]
           
            prediction = model_2_code_experience_y.predict(inputs)

            if prediction < 45000:
                prediction += 12932.31
                


        if st.button('Рассчитать зарплату'):
            pr = abs(prediction)
            if pr < 10000: pr += 13041.49832
            if flag == 0:
                p1 = pr - model_0_code_experience_y_rmse/2
                p2 = pr +model_0_code_experience_y_rmse/2
            
            if flag == 1:
                p1 = pr - model_1_code_experience_y_rmse/2
                p2 = pr +model_1_code_experience_y_rmse/2
            
            if flag == 2:
                p1 = pr - model_2_code_experience_y_rmse/2
                p2 = pr +model_2_code_experience_y_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(p1, -1),2))} - {'{:.2f}'.format(round(np.squeeze(p2, -1),2))} рублей")
    else:
        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 3
            inputs = [1 if i in base_skills_0 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_n_sorted if x != 'v3_region_index']]
           

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_0_code_experience_n_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_0_code_experience_n_sorted_mask]
            prediction = model_0_code_experience_n.predict(inputs)
        

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 4
            inputs = [1 if i in base_skills_1 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_n_sorted if x != 'v3_region_index']]
            

            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))

            reg = data[str(option)]
            inputs.insert(model_1_code_experience_n_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_1_code_experience_n_sorted_mask]
            prediction = model_1_code_experience_n.predict(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 5
            inputs = [1 if i in base_skills_2 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_n_sorted if x != 'v3_region_index']]
            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))

            
            reg = data[str(option)]
            inputs.insert(model_2_code_experience_n_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_2_code_experience_n_sorted_mask]
            prediction = model_2_code_experience_n.predict(inputs)

            if prediction < 45000:
                prediction += 12932.31
                


        if st.button('Рассчитать зарплату'):
            pr = abs(prediction)
            if pr < 10000: pr += 13041.49832
            
            if flag == 3:
                p1 = pr - model_0_code_experience_n_rmse/2
                p2 = pr +model_0_code_experience_n_rmse/2
            
            if flag == 4:
                p1 = pr - model_1_code_experience_n_rmse/2
                p2 = pr +model_1_code_experience_n_rmse/2
            
            if flag == 5:
                p1 = pr - model_2_code_experience_n_rmse/2
                p2 = pr +model_2_code_experience_n_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(p1, -1),2))} - {'{:.2f}'.format(round(np.squeeze(p2, -1),2))} рублей")

    if flag == 0:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Без опытa")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

        prices = json.load(open(f'{name}/model_0_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
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

        prices = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
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


        prices = json.load(open(f'{name}/model_2_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
    if flag == 3:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open(f'{name}/model_0_code_experience_n_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
    if flag == 4:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open(f'{name}/model_1_code_experience_n_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
    if flag == 5:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open(f'{name}/model_2_code_experience_n_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

elif inp_species == 'слесарь':

    name = 'slesar'
    model_0_code_experience_y_sorted = list(json.load(open(f'{name}/model_0_code_experience_y_{name}.json')).keys())
    model_1_code_experience_y_sorted = list(json.load(open(f'{name}/model_1_code_experience_y_{name}.json')).keys())
    model_2_code_experience_y_sorted = list(json.load(open(f'{name}/model_2_code_experience_y_{name}.json')).keys())
    model_0_code_experience_n_sorted = list(json.load(open(f'{name}/model_0_code_experience_n_{name}.json')).keys())
    model_1_code_experience_n_sorted = list(json.load(open(f'{name}/model_1_code_experience_n_{name}.json')).keys())
    model_2_code_experience_n_sorted = list(json.load(open(f'{name}/model_2_code_experience_n_{name}.json')).keys())
    
    model_0_code_experience_y_rmse = 5653
    model_1_code_experience_y_rmse = 19276
    model_2_code_experience_y_rmse = 9349
    model_0_code_experience_n_rmse = 15676
    model_1_code_experience_n_rmse = 13269
    model_2_code_experience_n_rmse = 15580

    base_skills_0 = [x.strip() for x in open(f'{name}/base_skills_0_{name}.txt', 'r') if len(x) > 3]
    base_skills_1 = [x.strip() for x in open(f'{name}/base_skills_1_{name}.txt', 'r') if len(x) > 3]
    base_skills_2 = [x.strip() for x in open(f'{name}/base_skills_2_{name}.txt', 'r') if len(x) > 3]
    
    model_0_code_experience_y = CatBoostRegressor()
    model_0_code_experience_y.load_model(f'{name}/model_0_code_experience_y_{name}')
    model_1_code_experience_y = CatBoostRegressor()
    model_1_code_experience_y.load_model(f'{name}/model_1_code_experience_y_{name}')
    model_2_code_experience_y = CatBoostRegressor()
    model_2_code_experience_y.load_model(f'{name}/model_2_code_experience_y_{name}')
    model_0_code_experience_n = CatBoostRegressor()
    model_0_code_experience_n.load_model(f'{name}/model_0_code_experience_n_{name}')
    model_1_code_experience_n = CatBoostRegressor()
    model_1_code_experience_n.load_model(f'{name}/model_1_code_experience_n_{name}')
    model_2_code_experience_n = CatBoostRegressor()
    model_2_code_experience_n.load_model(f'{name}/model_2_code_experience_n_{name}')

    m_order = [x.strip() for x in open(f'{name}/order_{name}.txt')]
    model_0_code_experience_y_sorted_mask = [model_0_code_experience_y_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_1_code_experience_y_sorted_mask = [model_1_code_experience_y_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_2_code_experience_y_sorted_mask = [model_2_code_experience_y_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_0_code_experience_n_sorted_mask = [model_0_code_experience_n_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_1_code_experience_n_sorted_mask = [model_1_code_experience_n_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_2_code_experience_n_sorted_mask = [model_2_code_experience_n_sorted.index(m_order[i]) for i in range(len(m_order))]

    
    st.header(f"Оценка стоимости навыков {inp_species}")
    # data = pd.read_csv("fish.csv")

    st.subheader("Выберите опыт работы")
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        experience = st.radio(
            'опыт работы:',
            np.unique(['Без опыта', 'От 1 до 3 лет','От 3 лет']))

    f = open('regions_final.json')
    data = json.load(f)

    vahta = 1 if st.checkbox('Вахта') else 0
    if vahta:
        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 0
            inputs = [1 if i in base_skills_0 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_y_sorted if x != 'v3_region_index']]
            
            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))

            reg = data[str(option)]
            inputs.insert(model_0_code_experience_y_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_0_code_experience_y_sorted_mask]
            prediction = model_0_code_experience_y.predict(inputs)
        

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 1
            inputs = [1 if i in base_skills_1 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_y_sorted if x != 'v3_region_index']]
            

            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_1_code_experience_y_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_1_code_experience_y_sorted_mask]
            prediction = model_1_code_experience_y.predict(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 2
            inputs = [1 if i in base_skills_2 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_y_sorted if x != 'v3_region_index']]
            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_2_code_experience_y_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_2_code_experience_y_sorted_mask]
            prediction = model_2_code_experience_y.predict(inputs)

            if prediction < 45000:
                prediction += 12932.31
                


        if st.button('Рассчитать зарплату'):
            pr = abs(prediction)
            if pr < 10000: pr += 13041.49832
            if flag == 0:
                p1 = pr - model_0_code_experience_y_rmse/2
                p2 = pr +model_0_code_experience_y_rmse/2
            
            if flag == 1:
                p1 = pr - model_1_code_experience_y_rmse/2
                p2 = pr +model_1_code_experience_y_rmse/2
            
            if flag == 2:
                p1 = pr - model_2_code_experience_y_rmse/2
                p2 = pr +model_2_code_experience_y_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(p1, -1),2))} - {'{:.2f}'.format(round(np.squeeze(p2, -1),2))} рублей")
    else:
        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 3
            inputs = [1 if i in base_skills_0 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_n_sorted if x != 'v3_region_index']]
            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_0_code_experience_n_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_0_code_experience_n_sorted_mask]
            prediction = model_0_code_experience_n.predict(inputs)
        

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 4
            inputs = [1 if i in base_skills_1 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_n_sorted if x != 'v3_region_index']]
            
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))

            reg = data[str(option)]
            inputs.insert(model_1_code_experience_n_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_1_code_experience_n_sorted_mask]
            prediction = model_1_code_experience_n.predict(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 5
            inputs = [1 if i in base_skills_2 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_n_sorted if x != 'v3_region_index']]
            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_2_code_experience_n_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_2_code_experience_n_sorted_mask]
            prediction = model_2_code_experience_n.predict(inputs)

            if prediction < 45000:
                prediction += 12932.31
                


        if st.button('Рассчитать зарплату'):
            pr = abs(prediction)
            if pr < 10000: pr += 13041.49832
            
            if flag == 3:
                p1 = pr - model_0_code_experience_n_rmse/2
                p2 = pr +model_0_code_experience_n_rmse/2
            
            if flag == 4:
                p1 = pr - model_1_code_experience_n_rmse/2
                p2 = pr +model_1_code_experience_n_rmse/2
            
            if flag == 5:
                p1 = pr - model_2_code_experience_n_rmse/2
                p2 = pr +model_2_code_experience_n_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(p1, -1),2))} - {'{:.2f}'.format(round(np.squeeze(p2, -1),2))} рублей")

    if flag == 0:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Без опытa")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

        prices = json.load(open(f'{name}/model_0_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
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

        prices = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
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


        prices = json.load(open(f'{name}/model_2_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
    if flag == 3:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open(f'{name}/model_0_code_experience_n_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
    if flag == 4:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open(f'{name}/model_1_code_experience_n_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
    if flag == 5:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open(f'{name}/model_2_code_experience_n_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

elif inp_species == 'специалист по персоналу':
    name = 'hr'
    model_0_code_experience_y_sorted = list(json.load(open(f'{name}/model_0_code_experience_y_{name}.json')).keys())
    model_1_code_experience_y_sorted = list(json.load(open(f'{name}/model_1_code_experience_y_{name}.json')).keys())
    model_2_code_experience_n_sorted = list(json.load(open(f'{name}/model_2_code_experience_y_{name}.json')).keys())
    model_0_code_experience_n_sorted = list(json.load(open(f'{name}/model_0_code_experience_n_{name}.json')).keys())
    model_1_code_experience_n_sorted = list(json.load(open(f'{name}/model_1_code_experience_n_{name}.json')).keys())
    
    model_0_code_experience_y_rmse = 7314
    model_1_code_experience_y_rmse = 6689
    model_2_code_experience_n_rmse = 10781
    model_0_code_experience_n_rmse = 10024
    model_1_code_experience_n_rmse = 11179

    base_skills_0 = [x.strip() for x in open(f'{name}/base_skills_0_{name}.txt', 'r') if len(x) > 3]
    base_skills_1 = [x.strip() for x in open(f'{name}/base_skills_1_{name}.txt', 'r') if len(x) > 3]
    base_skills_2 = [x.strip() for x in open(f'{name}/base_skills_2_{name}.txt', 'r') if len(x) > 3]
    
    model_0_code_experience_y = CatBoostRegressor()
    model_0_code_experience_y.load_model(f'{name}/model_0_code_experience_y_{name}')
    model_1_code_experience_y = CatBoostRegressor()
    model_1_code_experience_y.load_model(f'{name}/model_1_code_experience_y_{name}')
    model_2_code_experience_n = CatBoostRegressor()
    model_2_code_experience_n.load_model(f'{name}/model_2_code_experience_y_{name}')
    model_0_code_experience_n = CatBoostRegressor()
    model_0_code_experience_n.load_model(f'{name}/model_0_code_experience_n_{name}')
    model_1_code_experience_n = CatBoostRegressor()
    model_1_code_experience_n.load_model(f'{name}/model_1_code_experience_n_{name}')

    m_order = [x.strip() for x in open(f'{name}/order_{name}.txt')]
    model_0_code_experience_y_sorted_mask = [model_0_code_experience_y_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_1_code_experience_y_sorted_mask = [model_1_code_experience_y_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_2_code_experience_n_sorted_mask = [model_2_code_experience_n_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_0_code_experience_n_sorted_mask = [model_0_code_experience_n_sorted.index(m_order[i]) for i in range(len(m_order))]
    model_1_code_experience_n_sorted_mask = [model_1_code_experience_n_sorted.index(m_order[i]) for i in range(len(m_order))]

    
    st.header(f"Оценка стоимости навыков {inp_species}")
    # data = pd.read_csv("fish.csv")

    

    f = open('regions_final.json')
    data = json.load(f)

    vahta = 1 if st.checkbox('Дистанционно') else 0
    if vahta:
        st.subheader("Выберите опыт работы")
        left_column1, right_column1 = st.columns(2)
        with left_column1:
            experience = st.radio(
                'опыт работы:',
                np.unique(['Без опыта', 'От 1 до 3 лет']))


        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 0
            inputs = [1 if i in base_skills_0 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_y_sorted if x != 'v3_region_index']]
            
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_0_code_experience_y_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_0_code_experience_y_sorted_mask]
            prediction = model_0_code_experience_y.predict(inputs)
        

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 1
            inputs = [1 if i in base_skills_1 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_y_sorted if x != 'v3_region_index']]
            

            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_1_code_experience_y_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_1_code_experience_y_sorted_mask]
            prediction = model_1_code_experience_y.predict(inputs)

                


        if st.button('Рассчитать зарплату'):
            pr = abs(prediction)
            if pr < 10000: pr += 13041.49832
            if flag == 0:
                p1 = pr - model_0_code_experience_y_rmse/2
                p2 = pr +model_0_code_experience_y_rmse/2
            
            if flag == 1:
                p1 = pr - model_1_code_experience_y_rmse/2
                p2 = pr +model_1_code_experience_y_rmse/2
            
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(p1, -1),2))} - {'{:.2f}'.format(round(np.squeeze(p2, -1),2))} рублей")
    else:

        st.subheader("Выберите опыт работы")
        left_column1, right_column1 = st.columns(2)
        with left_column1:
            experience = st.radio(
                'опыт работы:',
                np.unique(['Без опыта', 'От 1 до 3 лет','От 3 лет']))

        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 3
            
            inputs = [1 if i in base_skills_0 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_n_sorted if x != 'v3_region_index']]
            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_0_code_experience_n_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_0_code_experience_n_sorted_mask]
            prediction = model_0_code_experience_n.predict(inputs)
        

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 4
            inputs = [1 if i in base_skills_1 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_n_sorted if x != 'v3_region_index']]
            
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_1_code_experience_n_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_1_code_experience_n_sorted_mask]
            prediction = model_1_code_experience_n.predict(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 2
            inputs = [1 if i in base_skills_2 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_n_sorted if x != 'v3_region_index']]
            

            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(data.keys()) if x in rus_regs]))


            reg = data[str(option)]
            inputs.insert(model_2_code_experience_n_sorted.index('v3_region_index'),reg)
            inputs = np.array(inputs)[model_2_code_experience_n_sorted_mask]
            prediction = model_2_code_experience_n.predict(inputs)     


        if st.button('Рассчитать зарплату'):
            pr = abs(prediction)
            if pr < 10000: pr += 13041.49832
            
            if flag == 3:
                p1 = pr - model_0_code_experience_n_rmse/2
                p2 = pr +model_0_code_experience_n_rmse/2
            
            if flag == 4:
                p1 = pr - model_1_code_experience_n_rmse/2
                p2 = pr +model_1_code_experience_n_rmse/2
            
            if flag == 5:
                p1 = pr - model_2_code_experience_n_rmse/2
                p2 = pr +model_2_code_experience_n_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(round(np.squeeze(p1, -1),2))} - {'{:.2f}'.format(round(np.squeeze(p2, -1),2))} рублей")

    if flag == 0:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Без опытa")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

        prices = json.load(open(f'{name}/model_0_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
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

        prices = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
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


        prices = json.load(open(f'{name}/model_2_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
    if flag == 3:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open(f'{name}/model_0_code_experience_n_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
    if flag == 4:
        st.subheader("")
        st.subheader("")
        st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

        st.write("Подсчет стоимости каждого навыка производился по формуле:")
        st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
        st.write("")
        st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


        prices = json.load(open(f'{name}/model_1_code_experience_n_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)
    

elif inp_species == 'продавец':
    name = 'prodavets'
    model_0_code_experience_sorted = list(json.load(open(f'{name}/model_0_code_experience_y_{name}.json')).keys())
    model_1_code_experience_sorted = list(json.load(open(f'{name}/model_1_code_experience_y_{name}.json')).keys())
    model_2_code_experience_sorted = list(json.load(open(f'{name}/model_2_code_experience_y_{name}.json')).keys())
    model_0_code_experience_rmse = 6159.105
    model_2_code_experience_rmse = 6842.395
    model_1_code_experience_rmse = 7072.589
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

    st.subheader("Выберите опыт работы")
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

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
    
        flag = 0
        inputs = [1 if i in base_skills_0 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_sorted if x != 'v3_region_index']]
            
        

        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            ([x for x in list(data.keys()) if x in rus_regs]))


        reg = data[str(option)]
        inputs.insert(model_0_code_experience_sorted.index('v3_region_index'),reg)
        inputs = np.array(inputs)[model_0_code_experience_sorted_mask]
        prediction = model_0_code_experience.predict(inputs)
    

    elif experience == 'От 1 до 3 лет':
        st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
        for number,skill in enumerate(base_skills_1):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

    
        flag = 1
        inputs = [1 if i in base_skills_1 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_sorted if x != 'v3_region_index']]
        
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            ([x for x in list(data.keys()) if x in rus_regs]))


        reg = data[str(option)]
        inputs.insert(model_1_code_experience_sorted.index('v3_region_index'),reg)
        inputs = np.array(inputs)[model_1_code_experience_sorted_mask]
        prediction = model_1_code_experience.predict(inputs)


    else:
        st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
        for number,skill in enumerate(base_skills_2):
            st.write(f'{number+1}) {skill}')

        st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        flag = 2
        inputs = [1 if i in base_skills_2 else 1 if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_sorted if x != 'v3_region_index']]
        
    
        st.subheader("Выберите регион вакансии")
        option = st.selectbox(
            'Напишите регион вакансии',
            ([x for x in list(data.keys()) if x in rus_regs]))


        reg = data[str(option)]
        inputs.insert(model_2_code_experience_sorted.index('v3_region_index'),reg)
        inputs = np.array(inputs)[model_2_code_experience_sorted_mask]
        prediction = model_2_code_experience.predict(inputs)

       
            


    if st.button('Рассчитать зарплату'):
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

        prices = json.load(open(f'{name}/model_0_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
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

        prices = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
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


        prices = json.load(open(f'{name}/model_2_code_experience_y_{name}.json'))
        dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
        fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
        st.plotly_chart(fig, use_container_width=False)
        st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

        fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
        st.plotly_chart(fig1, use_container_width=False)

elif inp_species == 'слесарь КИПиА':
    name = 'slesar_KIPiA'
    model_0_code_experience_y_sorted = json.load(open(f'{name}/model_0_code_experience_y_{name}.json'))
    model_1_code_experience_y_sorted = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))
    model_2_code_experience_y_sorted = json.load(open(f'{name}/model_2_code_experience_y_{name}.json'))
    model_0_code_experience_n_sorted = json.load(open(f'{name}/model_0_code_experience_n_{name}.json'))
    model_1_code_experience_n_sorted = json.load(open(f'{name}/model_1_code_experience_n_{name}.json'))
    model_2_code_experience_n_sorted = json.load(open(f'{name}/model_2_code_experience_n_{name}.json'))

    model_0_code_experience_y_sorted_obl = json.load(open(f'{name}/model_0_code_experience_y_{name}_obl.json'))
    model_1_code_experience_y_sorted_obl = json.load(open(f'{name}/model_1_code_experience_y_{name}_obl.json'))
    model_2_code_experience_y_sorted_obl = json.load(open(f'{name}/model_2_code_experience_y_{name}_obl.json'))
    model_0_code_experience_n_sorted_obl = json.load(open(f'{name}/model_0_code_experience_n_{name}_obl.json'))
    model_1_code_experience_n_sorted_obl = json.load(open(f'{name}/model_1_code_experience_n_{name}_obl.json'))
    model_2_code_experience_n_sorted_obl = json.load(open(f'{name}/model_2_code_experience_n_{name}_obl.json'))
    
    rmses = [float(x.strip()) for x in open(f'{name}/rmse_{name}.txt')]
    bases = [float(x.strip()) for x in open(f'{name}/base_{name}.txt')]

    model_0_code_experience_y_rmse = rmses[0]
    model_0_code_experience_n_rmse = rmses[1]
    model_1_code_experience_y_rmse = rmses[2]
    model_1_code_experience_n_rmse = rmses[3]
    model_2_code_experience_y_rmse = rmses[4]
    model_2_code_experience_n_rmse = rmses[5]

    base_skills_0 = [x.strip() for x in open(f'{name}/base_skills_0_{name}.txt', 'r') if len(x) > 3]
    base_skills_1 = [x.strip() for x in open(f'{name}/base_skills_1_{name}.txt', 'r') if len(x) > 3]
    base_skills_2 = [x.strip() for x in open(f'{name}/base_skills_2_{name}.txt', 'r') if len(x) > 3]

    m_order = [x.strip() for x in open(f'{name}/order_{name}.txt')]
    
    st.header(f"Оценка стоимости навыков {inp_species}")

    st.subheader("Выберите опыт работы")
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        experience = st.radio(
            'опыт работы:',
            np.unique(['Без опыта', 'От 1 до 3 лет','От 3 лет']))

    f = open('regions_final.json')
    data = json.load(f)

    vahta = 1 if st.checkbox('Вахта') else 0
    if vahta:
        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 0
            inputs = [model_0_code_experience_y_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_y_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_0_code_experience_y_sorted_obl.keys())]))

            reg = model_0_code_experience_y_sorted_obl[option]
            inputs += [reg]
            prediction = bases[0] + sum(inputs)
            

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 1
            inputs = [model_1_code_experience_y_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_y_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_1_code_experience_y_sorted_obl.keys())]))

            reg = model_1_code_experience_y_sorted_obl[option]
            inputs += [reg]
            prediction = bases[2] + sum(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 2
            inputs = [model_2_code_experience_y_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_y_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_2_code_experience_y_sorted_obl.keys())]))

            reg = model_2_code_experience_y_sorted_obl[option]
            inputs += [reg]
            prediction = bases[4] + sum(inputs)

                
        if st.button('Рассчитать зарплату'):
            pr = abs(prediction)
            if flag == 0:
                p1 = pr - model_0_code_experience_y_rmse/2
                p2 = pr +model_0_code_experience_y_rmse/2
            
            if flag == 1:
                p1 = pr - model_1_code_experience_y_rmse/2
                p2 = pr +model_1_code_experience_y_rmse/2
            
            if flag == 2:
                p1 = pr - model_2_code_experience_y_rmse/2
                p2 = pr +model_2_code_experience_y_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(p1)} - {'{:.2f}'.format(p2)} рублей")
    else:
        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 3
            inputs = [model_0_code_experience_n_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_n_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_0_code_experience_n_sorted_obl.keys())]))

            reg = model_0_code_experience_n_sorted_obl[option]
            inputs += [reg]
            prediction = bases[1] + sum(inputs)
        

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 4
            inputs = [model_1_code_experience_n_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_n_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_1_code_experience_n_sorted_obl.keys())]))

            reg = model_1_code_experience_n_sorted_obl[option]
            inputs += [reg]
            prediction = bases[3] + sum(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 5
            inputs = [model_2_code_experience_n_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_n_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_2_code_experience_n_sorted_obl.keys())]))

            reg = model_2_code_experience_n_sorted_obl[option]
            inputs += [reg]
            prediction = bases[5] + sum(inputs)

        if st.button('Рассчитать зарплату'):
            pr = prediction
 
            
            if flag == 3:
                p1 = pr - model_0_code_experience_n_rmse/2
                p2 = pr +model_0_code_experience_n_rmse/2
            
            if flag == 4:
                p1 = pr - model_1_code_experience_n_rmse/2
                p2 = pr +model_1_code_experience_n_rmse/2
            
            if flag == 5:
                p1 = pr - model_2_code_experience_n_rmse/2
                p2 = pr +model_2_code_experience_n_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(p1)} - {'{:.2f}'.format(p2)} рублей")

    # if flag == 0:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Без опытa")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

    #     prices = json.load(open(f'{name}/model_0_code_experience_y_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")
    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)


    
    # if flag == 1:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} От 1 до 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

    #     prices = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)

    # if flag == 2:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_2_code_experience_y_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)
    # if flag == 3:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_0_code_experience_n_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)
    # if flag == 4:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_1_code_experience_n_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)
    # if flag == 5:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_2_code_experience_n_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)


elif inp_species == 'слесарь-ремонтник':
    name = 'slesar_remontnik'
    model_0_code_experience_y_sorted = json.load(open(f'{name}/model_0_code_experience_y_{name}.json'))
    model_1_code_experience_y_sorted = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))
    model_2_code_experience_y_sorted = json.load(open(f'{name}/model_2_code_experience_y_{name}.json'))
    model_0_code_experience_n_sorted = json.load(open(f'{name}/model_0_code_experience_n_{name}.json'))
    model_1_code_experience_n_sorted = json.load(open(f'{name}/model_1_code_experience_n_{name}.json'))
    model_2_code_experience_n_sorted = json.load(open(f'{name}/model_2_code_experience_n_{name}.json'))

    model_0_code_experience_y_sorted_obl = json.load(open(f'{name}/model_0_code_experience_y_{name}_obl.json'))
    model_1_code_experience_y_sorted_obl = json.load(open(f'{name}/model_1_code_experience_y_{name}_obl.json'))
    model_2_code_experience_y_sorted_obl = json.load(open(f'{name}/model_2_code_experience_y_{name}_obl.json'))
    model_0_code_experience_n_sorted_obl = json.load(open(f'{name}/model_0_code_experience_n_{name}_obl.json'))
    model_1_code_experience_n_sorted_obl = json.load(open(f'{name}/model_1_code_experience_n_{name}_obl.json'))
    model_2_code_experience_n_sorted_obl = json.load(open(f'{name}/model_2_code_experience_n_{name}_obl.json'))
    
    rmses = [float(x.strip()) for x in open(f'{name}/rmse_{name}.txt')]
    bases = [float(x.strip()) for x in open(f'{name}/base_{name}.txt')]

    model_0_code_experience_y_rmse = rmses[0]
    model_0_code_experience_n_rmse = rmses[1]
    model_1_code_experience_y_rmse = rmses[2]
    model_1_code_experience_n_rmse = rmses[3]
    model_2_code_experience_y_rmse = rmses[4]
    model_2_code_experience_n_rmse = rmses[5]

    base_skills_0 = [x.strip() for x in open(f'{name}/base_skills_0_{name}.txt', 'r') if len(x) > 3]
    base_skills_1 = [x.strip() for x in open(f'{name}/base_skills_1_{name}.txt', 'r') if len(x) > 3]
    base_skills_2 = [x.strip() for x in open(f'{name}/base_skills_2_{name}.txt', 'r') if len(x) > 3]

    m_order = [x.strip() for x in open(f'{name}/order_{name}.txt')]
    
    st.header(f"Оценка стоимости навыков {inp_species}")

    st.subheader("Выберите опыт работы")
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        experience = st.radio(
            'опыт работы:',
            np.unique(['Без опыта', 'От 1 до 3 лет','От 3 лет']))

    f = open('regions_final.json')
    data = json.load(f)

    vahta = 1 if st.checkbox('Вахта') else 0
    if vahta:
        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 0
            inputs = [model_0_code_experience_y_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_y_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_0_code_experience_y_sorted_obl.keys())]))

            reg = model_0_code_experience_y_sorted_obl[option]
            inputs += [reg]
            prediction = bases[0] + sum(inputs)
            

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 1
            inputs = [model_1_code_experience_y_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_y_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_1_code_experience_y_sorted_obl.keys())]))

            reg = model_1_code_experience_y_sorted_obl[option]
            inputs += [reg]
            prediction = bases[2] + sum(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 2
            inputs = [model_2_code_experience_y_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_y_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_2_code_experience_y_sorted_obl.keys())]))

            reg = model_2_code_experience_y_sorted_obl[option]
            inputs += [reg]
            prediction = bases[4] + sum(inputs)

                
        if st.button('Рассчитать зарплату'):
            pr = abs(prediction)
            if flag == 0:
                p1 = pr - model_0_code_experience_y_rmse/2
                p2 = pr +model_0_code_experience_y_rmse/2
            
            if flag == 1:
                p1 = pr - model_1_code_experience_y_rmse/2
                p2 = pr +model_1_code_experience_y_rmse/2
            
            if flag == 2:
                p1 = pr - model_2_code_experience_y_rmse/2
                p2 = pr +model_2_code_experience_y_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(p1)} - {'{:.2f}'.format(p2)} рублей")
    else:
        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 3
            inputs = [model_0_code_experience_n_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_n_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_0_code_experience_n_sorted_obl.keys())]))

            reg = model_0_code_experience_n_sorted_obl[option]
            inputs += [reg]
            prediction = bases[1] + sum(inputs)
        

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 4
            inputs = [model_1_code_experience_n_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_n_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_1_code_experience_n_sorted_obl.keys())]))

            reg = model_1_code_experience_n_sorted_obl[option]
            inputs += [reg]
            prediction = bases[3] + sum(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 5
            inputs = [model_2_code_experience_n_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_n_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_2_code_experience_n_sorted_obl.keys())]))

            reg = model_2_code_experience_n_sorted_obl[option]
            inputs += [reg]
            prediction = bases[5] + sum(inputs)

        if st.button('Рассчитать зарплату'):
            pr = prediction
 
            
            if flag == 3:
                p1 = pr - model_0_code_experience_n_rmse/2
                p2 = pr +model_0_code_experience_n_rmse/2
            
            if flag == 4:
                p1 = pr - model_1_code_experience_n_rmse/2
                p2 = pr +model_1_code_experience_n_rmse/2
            
            if flag == 5:
                p1 = pr - model_2_code_experience_n_rmse/2
                p2 = pr +model_2_code_experience_n_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(p1)} - {'{:.2f}'.format(p2)} рублей")

    # if flag == 0:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Без опытa")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

    #     prices = json.load(open(f'{name}/model_0_code_experience_y_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")
    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)


    
    # if flag == 1:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} От 1 до 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

    #     prices = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)

    # if flag == 2:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_2_code_experience_y_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)
    # if flag == 3:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_0_code_experience_n_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)
    # if flag == 4:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_1_code_experience_n_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)
    # if flag == 5:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_2_code_experience_n_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)

elif inp_species == 'Слесарь механосборочных работ (MCP)':
    name = 'slesar_mech'
    model_0_code_experience_y_sorted = json.load(open(f'{name}/model_0_code_experience_y_{name}.json'))
    model_1_code_experience_y_sorted = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))
    model_2_code_experience_y_sorted = json.load(open(f'{name}/model_2_code_experience_y_{name}.json'))
    model_0_code_experience_n_sorted = json.load(open(f'{name}/model_0_code_experience_n_{name}.json'))
    model_1_code_experience_n_sorted = json.load(open(f'{name}/model_1_code_experience_n_{name}.json'))
    model_2_code_experience_n_sorted = json.load(open(f'{name}/model_2_code_experience_n_{name}.json'))

    model_0_code_experience_y_sorted_obl = json.load(open(f'{name}/model_0_code_experience_y_{name}_obl.json'))
    model_1_code_experience_y_sorted_obl = json.load(open(f'{name}/model_1_code_experience_y_{name}_obl.json'))
    model_2_code_experience_y_sorted_obl = json.load(open(f'{name}/model_2_code_experience_y_{name}_obl.json'))
    model_0_code_experience_n_sorted_obl = json.load(open(f'{name}/model_0_code_experience_n_{name}_obl.json'))
    model_1_code_experience_n_sorted_obl = json.load(open(f'{name}/model_1_code_experience_n_{name}_obl.json'))
    model_2_code_experience_n_sorted_obl = json.load(open(f'{name}/model_2_code_experience_n_{name}_obl.json'))
    
    rmses = [float(x.strip()) for x in open(f'{name}/rmse_{name}.txt')]
    bases = [float(x.strip()) for x in open(f'{name}/base_{name}.txt')]

    model_0_code_experience_y_rmse = rmses[0]
    model_0_code_experience_n_rmse = rmses[1]
    model_1_code_experience_y_rmse = rmses[2]
    model_1_code_experience_n_rmse = rmses[3]
    model_2_code_experience_y_rmse = rmses[4]
    model_2_code_experience_n_rmse = rmses[5]

    base_skills_0 = [x.strip() for x in open(f'{name}/base_skills_0_{name}.txt', 'r') if len(x) > 3]
    base_skills_1 = [x.strip() for x in open(f'{name}/base_skills_1_{name}.txt', 'r') if len(x) > 3]
    base_skills_2 = [x.strip() for x in open(f'{name}/base_skills_2_{name}.txt', 'r') if len(x) > 3]

    m_order = [x.strip() for x in open(f'{name}/order_{name}.txt')]
    
    st.header(f"Оценка стоимости навыков {inp_species}")

    st.subheader("Выберите опыт работы")
    left_column1, right_column1 = st.columns(2)
    with left_column1:
        experience = st.radio(
            'опыт работы:',
            np.unique(['Без опыта', 'От 1 до 3 лет','От 3 лет']))

    f = open('regions_final.json')
    data = json.load(f)

    vahta = 1 if st.checkbox('Вахта') else 0
    if vahta:
        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 0
            inputs = [model_0_code_experience_y_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_y_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_0_code_experience_y_sorted_obl.keys())]))

            reg = model_0_code_experience_y_sorted_obl[option]
            inputs += [reg]
            prediction = bases[0] + sum(inputs)
            

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 1
            inputs = [model_1_code_experience_y_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_y_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_1_code_experience_y_sorted_obl.keys())]))

            reg = model_1_code_experience_y_sorted_obl[option]
            inputs += [reg]
            prediction = bases[2] + sum(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 2
            inputs = [model_2_code_experience_y_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_y_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_2_code_experience_y_sorted_obl.keys())]))

            reg = model_2_code_experience_y_sorted_obl[option]
            inputs += [reg]
            prediction = bases[4] + sum(inputs)

                
        if st.button('Рассчитать зарплату'):
            pr = abs(prediction)
            if flag == 0:
                p1 = pr - model_0_code_experience_y_rmse/2
                p2 = pr +model_0_code_experience_y_rmse/2
            
            if flag == 1:
                p1 = pr - model_1_code_experience_y_rmse/2
                p2 = pr +model_1_code_experience_y_rmse/2
            
            if flag == 2:
                p1 = pr - model_2_code_experience_y_rmse/2
                p2 = pr +model_2_code_experience_y_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(p1)} - {'{:.2f}'.format(p2)} рублей")
    else:
        if experience == 'Без опыта':
            st.subheader(f"Базовые навыки {inp_species} Без опыта:")
            for number,skill in enumerate(base_skills_0):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")
        
            flag = 3
            inputs = [model_0_code_experience_n_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_0_code_experience_n_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_0_code_experience_n_sorted_obl.keys())]))

            reg = model_0_code_experience_n_sorted_obl[option]
            inputs += [reg]
            prediction = bases[1] + sum(inputs)
        

        elif experience == 'От 1 до 3 лет':
            st.subheader(f"Базовые навыки {inp_species} От 1 до 3 лет:")
            for number,skill in enumerate(base_skills_1):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

        
            flag = 4
            inputs = [model_1_code_experience_n_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_1_code_experience_n_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_1_code_experience_n_sorted_obl.keys())]))

            reg = model_1_code_experience_n_sorted_obl[option]
            inputs += [reg]
            prediction = bases[3] + sum(inputs)


        else:
            st.subheader(f"Базовые навыки {inp_species} Более 3 лет опыта:")
            for number,skill in enumerate(base_skills_2):
                st.write(f'{number+1}) {skill}')

            st.subheader("Выберите навыки для подсчета зарплаты по вакансии. Расположены в порядке убывания абсолютной значимости (см. развернутый график внизу страницы)")

            flag = 5
            inputs = [model_2_code_experience_n_sorted[i] if st.checkbox(i) else 0 for \
                 i in [x for x in model_2_code_experience_n_sorted]]
        
       
            st.subheader("Выберите регион вакансии")
            option = st.selectbox(
                'Напишите регион вакансии',
                ([x for x in list(model_2_code_experience_n_sorted_obl.keys())]))

            reg = model_2_code_experience_n_sorted_obl[option]
            inputs += [reg]
            prediction = bases[5] + sum(inputs)

        if st.button('Рассчитать зарплату'):
            pr = prediction
 
            
            if flag == 3:
                p1 = pr - model_0_code_experience_n_rmse/2
                p2 = pr +model_0_code_experience_n_rmse/2
            
            if flag == 4:
                p1 = pr - model_1_code_experience_n_rmse/2
                p2 = pr +model_1_code_experience_n_rmse/2
            
            if flag == 5:
                p1 = pr - model_2_code_experience_n_rmse/2
                p2 = pr +model_2_code_experience_n_rmse/2
            
            
            st.write(f"Предполагаемая ЗП:  {'{:.2f}'.format(p1)} - {'{:.2f}'.format(p2)} рублей")

    # if flag == 0:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Без опытa")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

    #     prices = json.load(open(f'{name}/model_0_code_experience_y_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")
    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)


    
    # if flag == 1:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} От 1 до 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")

    #     prices = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)

    # if flag == 2:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_2_code_experience_y_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)
    # if flag == 3:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_0_code_experience_n_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)
    # if flag == 4:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_1_code_experience_n_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)
    # if flag == 5:
    #     st.subheader("")
    #     st.subheader("")
    #     st.subheader(f"Гистограмма стоимости навыков {inp_species} Более 3 лет опыта")

    #     st.write("Подсчет стоимости каждого навыка производился по формуле:")
    #     st.write("(Зарплата по вакансии с выделенным навыком) - (Средняя зарплата с базовыми навыками)")
    #     st.write("")
    #     st.write("Чтобы полность изучить график, расширьте его. При наведении курсора на каждый столбец будет появляться доп. информация")


    #     prices = json.load(open(f'{name}/model_2_code_experience_n_{name}.json'))
    #     dfx = pd.DataFrame([int(x) for x in prices.values()],index = [x for x  in prices.keys()],columns = ['Стоимость навыка'])
    #     fig = px.histogram(dfx,x = dfx['Стоимость навыка'],y = dfx.index,  width=2000, height=2000,labels={'x':'Абсолютное отклонение от средней зп, создаваемое навыком', 'y':'Навык'})
    #     st.plotly_chart(fig, use_container_width=False)
    #     st.write("обязательно разверните график, нажав на значок стрелок, чтобы ознакомиться с информацией")

    #     fig1 = px.pie(dfx,values = dfx['Стоимость навыка'],names = dfx.index,  width=1300, height=1300,title = 'Отношение стоимости признаков')
    #     st.plotly_chart(fig1, use_container_width=False)