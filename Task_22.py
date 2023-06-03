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

def duplicate_numbers_in_the_list():
    first_len = int(input("Введите кол-во элементов первого множества: "))
    second_len = int(input("Введите кол-во элементов второго множества: "))

    first_list = list(map(str, input("Первое множество(через пробел): ").split()))
    second_list = list(map(str, input("Второе множество(через пробел): ").split()))

    if (len(first_list) != first_len) and (len(second_list) != second_len):
        raise Exception("Длины множеств не совпадают указанному кол-ву элементов")
    
    result_list = []
    
    for num in first_list:
        if num in second_list:
            result_list.append(num)

    result_list.sort()

    return result_list


print(duplicate_numbers_in_the_list())