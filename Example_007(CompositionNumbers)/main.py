#2.	Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def factorial(num, count = 1):
    for i in range(1, num + 1):
        count *= i
    return count

n = int(input('Введите число, до которого нужно вывести произведения чисел: '))
print(f'Набор произведений от "1" до "{n}" = ', end = '')
for i in range(1, n + 1):
    if i == n: 
        print(f'{factorial(i)}')
    else:
        print(f'{factorial(i)}', end = ', ')
