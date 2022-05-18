def sort(arg):
    for i in range(len(arg) - 1):
        j = i - 1
        a = arg[i]
        while arg[j] > a and j >= 0:
            arg[j + 1] = arg[j]
            j -= 1
        arg[j + 1] = a
    return arg

print('Введите количество элементов массива')
k = int(input())
print('Введите элементы массива')
b = []
for i in range(k):
    b.append(int(input()))
    
print(sort(b))
