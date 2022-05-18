import math #импортируем билиотеку для использования математических функций

#первая (исходная) функция
def f1(a, x, n):
    return ((x**(1/a)*math.tan(x)**3)/((5.73*n)**(1/5)))*((math.log(x)/2)+abs(a))*11.7


#вторая функция, которая зависит от условий
def f2(a, x):
    if (abs(x )> 1) and (a > 0):
        return abs(x)
    elif (abs(x) <= 1) and (a > 0):
        return 1 + x
    else:
        return math.sin(x)

#вычисление суммы ряда
def r(n):
    s = 0
    for i in range(1,n):
        s += ((2*i - 1)*0.5**(i - 1))
    return s

#вывод данных
print("a x n через пробел")
a,x,n = map(float,input().split())
print(f1(a,x,n))
print("a,x через пробел")
a,x = map(float,input().split())
print(f2(a,x))
print("n")
print(r(int(input())))
