#1
def area(figure, data):
    if figure == 'circle':
        res = 3.14*(data[0]**2)
    if figure == 'square':
        a,b = data
        res = a*b
    if figure == 'triangle':
        a,b = data
        res = (a*b)/2
    return ' Area {} = {}'.format(figure, res)
    
figure = input('figures >>>  ')
data = [ float(i) for i in input('input values  >>> ').rsplit()]
print(area(figure, data))

#2
x1 = int(input("Введите количество элементов в первом списке "))
#создаем пустые списки
m1 = []
m2 = []
m3 = []
for i in range(x1):
   m1.append(int(input()))
s1,s2,s3= 0,0,0 #переменные для сумм
for i in range(x1): #находим сумму элементов первого массива
   s1+= m1[i]
print("Сумма элементов первого списка равна:",s1)
print("Среднее арифметическое первого списка равно",s1/x1)
x2 = int(input("Введите количество элементов во втором списке "))
for j in range(x2):
   m2.append(int(input()))
for j in range(x2): #находим сумму элементов первого массива
   s2 += m2[j]
print("Сумма элементов второго списка равна:",s2)
print("Среднее арифметическое второго списка равно",s2/x2)
x3 = int(input("Введите количество элементов в третьем списке "))
for k in range(x3):
   m3.append(int(input()))
for k in range(x3): #находим сумму элементов первого массива
   s3 += m3[k]
print("Сумма элементов третьего списка равна:",s3)
print("Среднее арифметическое третьего списка равно",s3/x3)