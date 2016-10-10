x = int(input("Введите число от 1 до 9:"))
y = [n for n in range(1,4)]
z = [n for n in range(4,7)]
w = [n for n in range(7,10)]
if x in y:
    s = input('Введите строку:')
    p = int(input('Введите число повторов строки:'))
    i = 0
    while i < p:
        i = i+1
        print(s)
elif x in z:
    m = int(input('Введите степень, в которую следует возвести число:'))
    print(x**m)
elif x in w:
    i = 0
    while i<10:
        i = i+1
        x = x*1
        print(x)
else:
    print('Ошибка ввода!')

