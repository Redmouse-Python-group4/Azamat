def func(x):
    if x in range(0,8):
        return("Вам в детский сад")
    elif x in range(8,18):
        return('Вам в школу')
    elif x in range(18,25):
        return('Вам в пофессиональное учебное заведение')
    elif x in range(25,60):
        return('Вам на работу')
    elif x in range(60,120):
        return('Вам предостовляется выбор')
    else:
        i = 0
        while i<5:
            i = i+1
            return("Ошибка! Эта программа для людей!")
    
