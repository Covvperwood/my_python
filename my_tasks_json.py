

import json
def reader(filename):
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
    return numbers
def writer(filename, numbers):    
    with open(filename, 'w') as f_obj:
        json.dump(numbers, f_obj)

stop=1

tasks=reader('numbers.json')
while stop !=0:
    order=int(input('1. Добавить задачу \n2. Вывести список задач \n3. Выход \n')) 
    if order==1:
        category=str(input('Введите категорию задачи: \n'))
        name=str(input('Сформулируйте задачу:\n'))
        time=str(input('Добавьте время: \n'))
        tasks.append({'category': category, 'name': name, 'time': time})
    elif order==2:
        print(tasks)
    elif order==3:
        break

writer('numbers.json', tasks)
