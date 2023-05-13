"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""
#Решение1
S = int(input("Сумма чисел: "))
P = int(input("Произведение чисел: "))
for X in range(1001):
    for Y in range(1001):
        if P == X*Y and S == X+Y:
            print(X,Y)
            
#Решение2            
"""
x = int(input())
y = int(input())
for i in range(x):
for j in range(y):
if x == i + j and y == i * j:
print(i, j)
"""   

#Решение3
S = int(input("Сумма чисел: "))
P = int(input("Произведение чисел: "))
for i in range(S):                     #либо for i in range(S//2 + 1)
    if i * (S - i) == P:
        print(i, S - i)        

              