import pandas as pd
import json
import os

df = pd.DataFrame(columns = ['профессия','опыт работы']+[f'Навык_{i}' for i  in range(1,357)])
prof = [x for x in os.listdir('/Users/parlorsky/Desktop/vacancy_salary') if '.' not in x]
d = {'slesar_mech':'Слесарь-механик', 'medsestra':'Медсестра', 'slesar_instr':'Слесарь-инструментальщик', 'prodavets':'Продавец', 'slesar_KIPiA':'Слесарь-КИПиА', 'svarshik':'Сварщик', 'slesar':'Слесарь', 'slesar_remontnik':'Слесарь-ремонтник', 'buhgalter':'Бухгалтер', 'hr':'Специалист по персоналу'}
for i in prof:
    models = [x for x in os.listdir('/Users/parlorsky/Desktop/vacancy_salary/'+i) if 'model' in x and 'obl' not in x]
    for model in models:
        a = json.load(open('/Users/parlorsky/Desktop/vacancy_salary/'+i + '/' + model))
        stag = '0' if '0' in model else '1' if '1' in model else '2,3'
        vahta = '0' if len(models) == 3 else '1' if len(models) == 6 and 'y' in model else '0'
        if vahta == '0':
            if a[list(a.keys())[0]] > a[list(a.keys())[-1]]:
                print(1)
            else:
                print(0)
            mask = [d[i],stag] + [x for x in list(a.keys())]
            mask = mask + ['' for x in range(358-len(mask))]
            df.loc[len(df.index)] = mask
            
            

df.to_csv('ценность навыков по убыванию.csv',index = False,sep =';',encoding='utf-8-sig')
