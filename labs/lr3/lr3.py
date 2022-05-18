f = open("matrix.txt","r") #считываем файл
m = []
# считываем матрицу из файла в m
for l in f:
    m.append(list(map(int,l.split())))

# делаем суммы нужных диагоналей
n = len(m) # размерность матрицы
mm = 2*n-2 # количество диагоналей параллельных побочной (не включая ее саму)
s = [0]*mm # список сумм этих диагоналей

# вычисление
for k in range(n - 1):
    for i in range(k + 1):
        s[k] += abs(m[i][i])
for k in range(int(mm/2),mm):
    for i in range(int(k-mm/2+1),n):
        s[k] += abs(m[i][i])

print(min(s)) #вывод
