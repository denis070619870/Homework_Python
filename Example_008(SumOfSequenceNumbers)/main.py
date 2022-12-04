#	Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.

from msilib import sequence
n = int(input('Введите число до которого будет выводиться список: ')) 
def sequence_list(n):
    return [round((1 + 1 / x)**x, 3) 
    for x in range (1, n + 1)]

num = sequence_list(n)
print(num)
print(round(sum(num), 3))

