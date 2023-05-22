'''
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
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

read_array = read_int_from_console()
result_array = []
index_start = 0
index_end = len(read_array) - 1

#Если список четный то проходим половину элементов, если нечетный то int(bool(len(read_array) % 2)) добавит ещё еденичку
while index_start < int(len(read_array) / 2) + int(bool(len(read_array) % 2)):
    result_array.append(read_array[index_start] * read_array[index_end])
    index_start += 1
    index_end -= 1

print(result_array)