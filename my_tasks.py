from pprint import pprint
tasks=[{'name':'поздравить друга с днем рождения', 'category':'ДР', 'time':'12.12.2019 '},
         {'name':'купить масло', 'category':'покупки', 'time':'сегодня'}]

out=1
while out != 0 :
    a=int(input('1. Добавить задачу.\n2. Вывести список задач.\n3. Выход.\n'))
    if a==1:
        a=input('name: ')
        b=input('Category: ')
        c=input('time: ')
        tasks.append({'name ':a, 'category ':b, 'time ':c})
    elif a==2:
        pprint(tasks)
    elif a ==3:
        break

