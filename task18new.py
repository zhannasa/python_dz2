n = int(input('Enter the number of list elements: '))
a = []
for i in range(n):
    a.append(int(input()))
print(a)
x = int(input('Enter some number: '))
a.append(x)
print(a)
for i in range(0, len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
           a[i], a[j] = a[j], a[i]
print(a)
y = a.index(x)
z = y - 1
if y == 0:
    z = y + 1
print(a[z])