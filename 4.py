import csv


# открываем файл csv и создаём новый csv
with open('0students.csv') as file,open('0students_new.csv','w') as new_file:
    data = list(csv.reader(file,delimiter=';'))
    res = csv.writer(new_file,delimiter=';')
    data[0].append('login')
    data[0].append('password')
    res.writerow(data[0])
    for stroka in data[1:]:
        fio = stroka[1]
        login = create_login(fio)
        password = create_password()
        stroka.append(login)
        stroka.append([password])
        res.writerow(stroka)