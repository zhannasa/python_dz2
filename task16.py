# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
n = int(input('Enter the number of list elements: '))
a = []
for i in range(n):
    a.append(int(input()))
print(a)
x = int(input('Enter some number: '))
count = 0
for i in range(0, len(a)):
    if a[i] == x:
        count+=1
print(count)