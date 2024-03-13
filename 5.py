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
    hash_value = 0
    for c in s:
        hash_value += d[c] *p **i
        i+=1
    return hash_value % m
# encoding='utf-8' убрали и ; заменили  потому что файл другой
with open('0students.csv') as file,open('0students_new.csv','w') as new_file:
    data = list(csv.reader(file,delimiter=';'))
    res = csv.writer(new_file,delimiter=';')
    print(data[1])
    # for stroka in data[1:]:
