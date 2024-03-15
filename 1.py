import csv

#открываем файл и создаём новый
with open('students.csv',encoding='utf-8') as file,open('students_new1.csv','w',newline='') as new_file:
    data = list(csv.reader(file,delimiter=','))
    res = csv.writer(new_file, delimiter=';')

    # находим ученика
    chel = 'Хадаров Владимир'
    a = []
    for stroka in data[1:]:
        if chel in stroka[1]:
            print(f"Ты получил: {stroka[-1]}, за проект - {stroka[2]}")
        if stroka[4] != 'None':
            a.append(int(stroka[4]))

    # ищем среднее
    sred = round(sum(a)/len(a),3)

    # заполняем файл students_new.csv
    res.writerow(data[0])
    for stroka in data[1:]:
        if stroka[4] != 'None':
            res.writerow(stroka)
        else:
            stroka[4] = sred
            res.writerow(stroka)