import os 
import math 
import time
while True:
    print("Введите 1, если нужно очистить консоль")
    znak = input("Введи знак (+,-,*,/) ")
    if znak == "+":
        numb1 = int(input("Введи первое число "))
        numb2 = int(input("Введи второе число "))
        numb = numb1 + numb2 
        print("Ответ: ", int(numb))
    if znak == "-":
        numb1 = int(input("Введи первое число "))
        numb2 = int(input("Введи второе число "))
        numb = numb1 - numb2
        if numb1 <= numb2:
            print("Ошибка... ")
            print("Второе число больше первого. ")
            continue
        print("Ответ: ", int(numb))
    if znak == "*":
        numb1 = int(input("Введи первое число "))
        numb2 = int(input("Введи второе число "))
        numb = numb1 * numb2 
        print("Ответ: ", int(numb))
    if znak == "/":
        numb1 = int(input("Введи первое число "))
        numb2 = int(input("Введи второе число "))
        numb = numb1 / numb2 
        if numb1 < numb2:
            print("Ошибка... ")
            print("Второе число больше первого числа... ")
            continue 
        print("Ответ: ", int(numb))
    if znak == "1":
        os.system('clear')
        print("Консоль очищена... ")
        time.sleep(2)
        os.system('clear')
        continue