'''
2. Написать программу поиска самого длинного слова в строке,
разделенной точкой запятой.
'''
s = input('Введите строку разделенной пробелами, и программа выведет самое длинное слово:').replace(' ', ";")
maxlen = 0
word = s.split(';')
for i in word:
    if len(i) > maxlen:
        maxlen = len(i)
    else:
        pass
for i in word:
    if len(i) == maxlen:
        print("Самое длинное слово: %s" % i)
    else:
        pass
