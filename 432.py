import json
name = 'svarshik'

model_1_code_experience_y_sorted = json.load(open(f'{name}/model_1_code_experience_y_{name}.json'))

inputs = [model_1_code_experience_y_sorted[i] if 1 else 0 for \
                 i in [x for x in model_1_code_experience_y_sorted]]

print(inputs)