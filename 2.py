import csv

#функция поиска
def vstavka(data):
    for i in range(len(data)):
        temp = data[i]
        j = i-1



12
#открываем файл '0students.csv'
with open('0students.csv') as f:
    data = list(csv.reader(f,delimiter=';'))
    i_id = input()
    while i_id != 'СТОП':
        res = search(i_id,data)
        if res is None:
            print('Ничего не найдено')
        else:
            print(f'Проект № {i_id}  делал: {res[1]} он(а) получил(а) оценку - {res[-1]}')
        i_id = input()