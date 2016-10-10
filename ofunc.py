def func(x):
    if x in range(1,4):
        s = input('Введите строку:')
        p = int(input('Введите число повторов строки:'))
        return((s+'\n')*p)
    elif x in range(4,7):
        m = int(input('Введите степень, в которую следует возвести число:'))
        return(x**m)
    elif x in range(7,10):
        return((str(x)+'\n')*10)
    else:
        return('Ошибка ввода!')
