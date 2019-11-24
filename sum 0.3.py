while True:
    try:      
        print("********************************************")
        x = int(input("первая цифра: ")) #создание переменной
        simvol = input("символ: ")
        y = int(input("вторая цифра: "))
        
        if simvol == "+": #здесь проверка символа на плюс  
                print("otvet:", x+y)
        elif simvol == "-": #здесь проверка символа на минус
                print("otvet:", x-y)
        elif simvol == "*": #здесь проверка символа на умножение
                print("otvet:", x*y)
        elif simvol == "/": #здесь проверка символа на деление
                print("otvet:", x/y)
        else:
                print("я тaкого не умею")              
    except ValueError:
        print("ОШИБКА ВВОДА ЦИФР!")

