import csv

# словарь символов для hash
alf = sorted('йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ')
d = {alf[i]:i+1 for i in range(66)}


# функция задаёт строке уникальный хэш
# s - входная строка возвращает уникальный хэш этой строки
def hash(s):
    s = s.replace(' ','')
    p = 67
    m = (10**9)+9
    i  =0
    hash_value = 0
    for c in s:
        hash_value += d[c] *p **i
        i+=1
    return hash_value % m
# encoding='utf-8' убрали и ; заменили  потому что файл другой
# открываем файл csv и создаём новый csv
with open('0students.csv') as file,open('0students_new.csv','w') as new_file:
    data = list(csv.reader(file,delimiter=';'))
    res = csv.writer(new_file,delimiter=';')
    res.writerow(data[0])
    #меняем id на hash
    for stroka in data[1:]:
        fio =  stroka[1]
        h = hash(fio)
        stroka[0] = h
        res.writerow(stroka)
