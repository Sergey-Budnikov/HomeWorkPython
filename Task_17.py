"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем 
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""
a = [1, 1, 2, 5, 8, 9, 5, 14, 65]
b = []
for el in a:
    if(not el in b):
        b.append(el)
print(len(b))
print(len(set(a)))        
        