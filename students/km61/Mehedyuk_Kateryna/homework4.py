# your ---'Цикл while'---------------------------------------------------------

#task1
"""По данному целому числу N распечатайте все квадраты натуральных чисел, не превосходящие N, в порядке возрастания."""
N=int(input())
#int, тому що N==ціле число
x = 1
while (x**2) <=N:
    print(x ** 2)
    x += 1
#task2
"""Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от  1.""" 
number=int(input())
x=2
while number%x!=0:
        if number<2:
         break
        x+=1
else:
    print(x)
#task3
"""По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. Выведите показатель степени и саму степень."""
# Операцией возведения в степень пользоваться нельзя!
N=int(input())
#int, тому що N==ціле число
x=2
i=0
while x<=N:
    x*=2
    i+=1
else:
    print(i,x/2)
#task4
"""В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров."""
#Программа получает на вход действительные числа x и y и должна вывести одно натуральное число
x=int(input()) 
y=int(input())
#int, тому що x, y== числa
i=1
while x<y:
    i+=1
    x+=(0.1*x)
else:
    print(i)
#task6
"""Последовательность завершается числом 0, при считывании которого программа должна закончить свою работу и вывести количество членов последовательности (не считая завершающего числа 0)."""
#Программа получает на вход последовательность целых неотрицательных чисел, каждое число записано в отдельной строке.
x=1
i=0
while x>0:
    x=int(input())
    i+=1
print(i-1)
#task7
"""Определите сумму всех элементов последовательности, завершающейся числом 0."""
# В этой и во всех следующих задачах числа, следующие за первым нулем, учитывать не нужно
b=0
x=1
while x>0 or x<0:
    x=int(input())
    b+=x
print(b)
#task8
"""Определите среднее значение всех элементов последовательности, завершающейся числом 0."""
b=0
x=1
i=0
while x>0 or x<0:
    x=int(input())
#int, тому що х==число,що закінчується на 0
    b+=x
    i+=1
print(b/(i-1))
#task9
"""Последовательность состоит из натуральных чисел и завершается числом 0. Определите значение наибольшего элемента последовательности."""
x=1
b=0
while x>0:
    x=int(input())
#int, тому що х==число,що закінчується на 0
 if x>b:
        b=x
print(b)
#task10
""" Определите индекс наибольшего элемента последовательности. Если наибольших элементов несколько, выведите индекс первого из них. """
#Нумерация элементов начинается с нуля
x=1
b=0
i=0
i1=0
while x>0:
    x=int(input())
    i+=1
    if x>b:
        b=x
        i1=i
print(i1-1)
#task11
"""Определите количество четных элементов в последовательности, завершающейся числом 0."""
x=1
b=0
while x>0:
    x=int(input())
    if x%2==0:
        b+=1
print(b-1)
#task12
"""Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности больше предыдущего элемента."""
x=1
b=0
k=0
while x>0:
    x=int(input())
    z=x
    if k<x:
        k=x
        b+=1
else:
        k=z
print(b-1)
#task13
"""Последовательность состоит из различных натуральных чисел и завершается числом 0. Определите значение второго по величине элемента в этой последовательности."""
#Последовательность состоит из различных натуральных чисел и завершается числом 0
x=1
b=0
z=0
while x>0:
    x=int(input())
    if x>b:
        z=b
        b=x
    elif x>z:
        z=x

print(z)
#task14
"""Последовательность состоит из натуральных чисел и завершается числом 0. Определите, сколько элементов этой последовательности равны ее наибольшему элементу."""
x=1
b=0
i=0
while x>0:
    x=int(input())
    if b<x:
        b=x
        i=0
    elif x==b:
        i+=1
print(i+1)
code goes here