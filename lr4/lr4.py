import codecs
#сруктура данных студента
class StudStruct:
    def __init__(self, num, name, s1, s2, s3):
        self.num = num
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

f = codecs.open("Task4.txt",encoding = "utf-8") #считываем файл
a = []

#заполяем массив a новосозданными обьектами класса выше
for l in f:
    num,name,s1,s2,s3 = l.split()
    a.append(StudStruct(num,name,int(s1),int(s2),int(s3)))
f.close()

#записываем в файл тех студентов, у кого пять по физике
f = open("Task4out.txt","w")
for el in a:
    if el.s3 == 5:
        f.write(el.num+" "+el.name+" "+str(el.s1)+" "+str(el.s2)+" "+str(el.s3)+"\n")
f.close()
