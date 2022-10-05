# Дано
# 1.Есть два числа и знак,которые вводятся пользователем
# 2.Программа зациклена
# 3.Завершение программы на знак '0'
# 4.Введение неверного знака приводит к ошибке и повторному запросу
# 5.Сообщение о невозможности деления на 0(нуль)

# Задачи
# 1. правильный input
# 2. программу зациклить под while
# 3. Обработка запросов
# 4. перехват ошибок

def inputNum():
    num = 0
    while True:
        try:
            num = int(input("Введите число: "))
            break
        except ValueError:
            print("Вы ввели НЕ число,попробуйте ещё раз.")
    return num


def input_checkChar():
    check = False
    char = ''
    while check == False:
        char = input('''
1.Cложение - '+' ;
2.Вычитание - '-' ;
3.Умножение - '*' ;
4.Деление - '/' ;
5.Выход из программы - '0' .
Введите знак :''')
        if char != '+' and char != '-' and char != '*' and char != '/' and char != '0':
            print("Вы ввели направильный знак,попробуйте еще раз.")
        else:
            check = True
    return char


exit = False
while exit == False:
    num1 = inputNum()
    num2 = inputNum()
    char = input_checkChar()
    if char == '+':
        print("Сумма чисел: ", num1+num2)
    if char == '-':
        print("Разница чисел: ", num1-num2)
    if char == '*':
        print("Умножение чисел: ", num1*num2)
    if char == '/':
        if num1 * num2 == 0:
            print("Деление на нуль невозможно.")
        else:
            print("Деление чисел: ", num1/num2)
    if char=='0':
        print("Выход из программы.")
        exit=True
