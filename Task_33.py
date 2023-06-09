"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

from random import randint

list_1 = list(randint(1, 5) for i in range(int(input("Введите оличество элементов: "))))
print(list_1)

def change(List):
    min_num = min(List)
    max_num = max(List)
    for i in range(len(List)):
        if List[i] == max_num:
            List[i] = min_num
    return List     

print(change(list_1))