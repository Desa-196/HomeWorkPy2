#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def read_int_from_console(text):
    readInt = 0
    while(True):
        try:
            readInt = int(input(text))
        except:
            print('Введено не число!')
            continue
        if readInt > 0:
            return readInt
        else:
            print('Число должно быть больше 0!')

N = read_int_from_console('Введите число N: ')

result = 1
while result <= N:
    #Выводим степень, ', ' if result*2 <= N else '' что бы не отображать последнюю запятую
    print(result, ', ' if result*2 <= N else '', sep = '', end = '')
    result *= 2
