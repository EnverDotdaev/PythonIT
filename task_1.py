# TODO решите задачу
import json
def task() -> float:
    summa = 0
    with open('input.json', 'r') as file:
        data = json.load(file)
        for i in data:
            summa += i['score'] * i['weight']
    return round(summa, 3)
print(task())
