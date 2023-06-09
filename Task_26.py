"""Задача 26:  Посчитать факториал (произведение 1 до N)
и треугольное число (сумма чисел от 1 до N) для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов"""

def RecursFack(n):
    if n == 0:
        return 1
    else:
        return n * RecursFack(n - 1)

N = int(input())
print(RecursFack(N)) 


def RecursSum(n):
    if n == 1:
        return n
    else:
        return n + RecursSum(n - 1)

N = int(input())
print(RecursSum(N))  

"""Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., 
где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи"""   
 
def Fib(n):
    if n in [1, 2]:
        return 1
    return Fib(n - 1) + Fib(n - 2) 
N = int(input())
list_1 = []
for i in range(1, N + 1):
    list_1.append(Fib(i))
print(list_1) 
    