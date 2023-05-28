# Задача 18: Требуется найти в списке A самый близкий по величине элемент к заданному числу X. 
# ользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5
n = int(input('Enter the number of list elements: '))
a = []
for i in range(n):
    a.append(int(input()))
print(a)
x = int(input('Enter some number: '))
for i in range(0, len(a)):
    if a[i] == x - 1:
        print(a[i])    
    if a[i] == a[0]:
        print(x+1)
        