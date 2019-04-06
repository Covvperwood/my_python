try: ##конструкция для обнаружения ошибок о неисправности файла
    filepath = 'file.txt'
    with open(filepath, 'r') as fio:
        result = fio.readlines()
except BaseException as e:
    print("Сведения об ошибке", e)
    
import csv
def csv_reader(file_obj):
    with open(file_obj) as csvfile: ##Стандартные действия по открытию файла
        reader = csv.DictReader(csvfile) ##с помощью класса DictReader считываем информацию
        if not reader:
            raise Exception("File is empty")
        for row in reader: ##оформляем вывод для элементов
             print('name: ', row['name'],'address: ', row['address'],'age: ', row['age'])
csv_reader('file.txt')



##БОЛЕЕ КРИВОЙ, НО ТЕМ НЕ МЕНЕЕ РАБОТАЮЩИЙ ВАРИАНТ
##import csv
##def csv_reader_2(file_obj):
##    results = []
##    with open(file_obj) as File:
##        reader = csv.DictReader(File)
##        for row in reader:
##            results.append(row)
##        print(results)
##
##csv_reader_2('file.txt')



























