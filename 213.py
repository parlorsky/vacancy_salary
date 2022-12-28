import json
import random
path = '/Users/parlorsky/Desktop/vacancy_salary/svarshik/model_1_code_experience_y_svarshik_obl_.json'
f = open(path)
data = json.load(f)

data['Москва'] = max(data.values()) + random.randint(1500,2500)
print(data['Москва'])


json_object = json.dumps(data, indent=len(data))
with open(f"{path}", "a") as outfile:
    outfile.write(json_object)