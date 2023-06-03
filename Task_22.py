"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""
n = {2,5,7,45,67,23,12,78,4,44,444,500,1001}
m = {1,2,45,12,444,10,1001,500}
c = n.intersection(m)
print(c)
c = list(c)
print(c) 
list.sort(c)
print(c)

# num = int(input('Enter: '))
# n = set()
# list1 = []
# for i in range(num):
#     num = input('Enter: ')
#     list1.append(num) 
# print(list1) 
# n.update(list1)   
# print(n)

# num = int(input('Enter: '))
# m = set()
# list1 = []
# for i in range(num):
#     num = input('Enter: ')
#     list1.append(num) 
# print(list1) 
# m.update(list1)   
# print(m)
# c = n.intersection(m)
# print(c)
# c = list(c)
# print(c) 
# list.sort(c)
# print(c)