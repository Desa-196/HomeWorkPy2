'''
1 Задайте список из нескольких чисел. Напишите программу,
которая найдёт сумму элементов списка,
стоящих на нечётной позиции.
*Пример:*

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''

def read_int_from_console():
    read_array = []
    while True:
        readInt = 0
        while(True):
            read_string = input('Введите число или \'end\' для окончания ввода: ')

            if(read_string == 'end'): return read_array

            try:
                readInt = int(read_string)
            except:
                print('Введено не число!')
                continue
            read_array.append(readInt);

print(read_int_from_console())
