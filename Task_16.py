"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
Ввод: 5
Ввод: 3 2 3 7 5
Ввод: 3
-> 2
"""
# List = [1, 5, 5, 8, 12, 5, 44]
# count = 0
# for i in List:
#     if i == 5:
#         count+= 1
# print(count)
n = int(input("Enter number: "))
A = []
X = 0
for i in range(1, n + 1):
    N = int(input(f"{i}й элемент: "))
    A.append(N)
    if N == 3:
        X+= 1
print(A)        
print(X) 

# Второе рещение

n = int(input("Enter number: "))
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)
k = int(input())
print(list_1.count(k))       