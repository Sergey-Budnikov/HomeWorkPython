"""
Задача №37. Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3
"""
n = int(input("Enter A: "))
def rotate(n):
    if n == 0:
        return " "
    else:
        a = int(input("Value: "))
        return rotate(n - 1) + f"{a} "
print(rotate(n)) 

#РЕШЕНИЕ №2

def print_num(n):
    number = int(input(f"Enter value #{n} "))
    if n > 1:
        print_num(n - 1)
    print(number, end=" ")
n = int(input())
print_num(n)           