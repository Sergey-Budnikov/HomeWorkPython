"""
Задача 36. Напишите программу, которая на вход принимает два числа А и В,
и возводит число А в целую степень В с помощью рекурсии
"""

num1 = int(input("Enter A: "))
num2 = int(input("Enter B: "))
c = 1
def degree(a, b, c):
    if b != 0:
        c *= a
        b -= 1
    else:
        return c    
    return degree(a, b, c)    
print(degree(num1, num2, c))      
    
#РЕШЕНИЕ №2

def my_power(a,b):
    if b == 0:
        return 1
    else:
        return a * my_power(a,b-1)
    
a = int(input())
b = int(input())    
print(my_power(a,b))    
    
            