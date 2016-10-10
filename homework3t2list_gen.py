x = int(input("Введите число от 1 до 9:"))
if x in range(1,4):
        s = input("Введите строку:")
        n = int(input("Введите число повторов строки:"))
        i = 0
        while i < n:
            print(s)
            i = i+1
elif x in range(4,7):
    m = int(input('Введите степень, в которую следует возвести число:'))
    print(x**m)
elif x in range(7,10):
    i = 0
    while i < 10:
        i = i+1
        x = x*1
        print(x)
else:
    print('Ошибка ввода!')
