import csv

# словарь символов для hash
alf = sorted('йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ')
d = {alf[i]:i+1 for i in range(66)}


# функция задаёт строке уникальный хэш

def hash(s):
    s = s.replace(' ','')
    p = 67
    m = (10**9)+9
    hash_value = 0
    for c in s:
        hash_value += d[c] *p **i
        i+=1
    return hash_value % m