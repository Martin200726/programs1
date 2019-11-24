print("привет, я программа которая может возводить число в степень!")
while True:
    try:
        print("**********************************")
        x = int(input())
        y = int(input())
        print(x**y)
    
    except ValueError:
        print("ОШИБКА: введите число-покакзатель степени!")
