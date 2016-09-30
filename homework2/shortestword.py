'''1.Написать программу поиска самого короткого слова в строке,
разделенной пробелами.
'''
'''
# -*- coding: utf8 -*-
s = input('Введите строку разделенной пробелами, и программа выведет самое короткое слово:').split(' ')

w = 0
min_w = len(s)
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z' \
    or 'а'<=i<='я' or 'А'<=i<='Я':
        w += 1
    else:
        if w < min_w and w != 0:
            min_w = w
        w = 0
print(min_w)
'''
s = input('Введите строку разделенной пробелами, и программа выведет самое короткое слово:')
word = s.split(' ')
z = str(input('Введите знак, который выделиться со словом:'))
sortedlist = sorted(word, key=len)
for i in sortedlist:
    if len(sortedlist[0]) == len(i):
        print(i)
print('Самое короткое слово:',z+sortedlist[0]+z,)
