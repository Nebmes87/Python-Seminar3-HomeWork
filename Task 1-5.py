# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции. Пример:  
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def summ_numbers(some_list):
    summ = 0
    for i in range(1, len(some_list), 2):
        summ += some_list[i]
    
    return summ


my_list = [int(i) for i in input('Введите элементы списка через пробел: ').split()]
print(summ_numbers(my_list))

# Напишите программу, которая найдёт произведение
#  пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д. Пример:  
# [2, 3, 4, 5, 6] => [12, 15, 16];  [2, 3, 5, 6] => [12, 15]

import math

def complex_numbers(some_list):
    complex = []
    for i in range(math.ceil(len(some_list) / 2)):
        complex.append(some_list[i] * some_list[len(some_list) - i - 1])
    
    return complex


my_list = [int(i) for i in input('Введите элементы списка: ').split()]
print(complex_numbers(my_list))

# Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов. 
# Пример:  [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = ['1.1', '1.2', '3.1', '5.1', '10.01']
print(numbers)
num = []                        
for i in numbers:
    num.append(i.split('.'))    
print(num)    
for el in range(len(numbers)):  
    num[el] = num[el].pop()  
    num[el] = '0.' + num[el]   
    num[el] = float(num[el])  
result = max(num) - min(num)
print(num) 
print(result)

# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное. 
# Пример: 
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число в десятичной системе счисления: '))
binary = str(bin(number))
print(f'Число {number} в двоичной системе счисления --> {binary[2:]}')

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. 
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи]

num = int(input('Enter number Negafibonacci: '))
numbers = []           
numbers.append(0)
numbers.append(1)
for i in range(2,num +1):
    numbers.append((numbers[i-1] + numbers[i-2]))

numbers_neg = []                  
numbers_neg.append(1)
numbers_neg.append(1)
for i in range(2,num):
    numbers_neg.append((numbers_neg[i-1] + numbers_neg[i-2]))
for i in range(len(numbers_neg)):             
    numbers_neg[i] = ((-1)**i) * numbers_neg[i]
    
numbers_neg.reverse()               
res = numbers_neg + numbers         
print(numbers)
print(numbers_neg)
print ('negafibonacci = ', res)