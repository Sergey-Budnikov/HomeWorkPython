"""
Задача 10: На столе лежат n монеток. 
Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть.
"""
n = int(input('Количство монет: '))
# countorel = 0
# countreshka = 0 
# for i in range(1, n + 1):
#     k = int(input(f'{i}я монета: '))  
#     if k == 0:
#         countorel+= 1
#     else:    
#         countreshka+= 1 
countorel = 0
countreshka = 0
i = 1  
while i <= n:
    k = int(input(f'{i}я монета: '))  
    if k == 0:
        countorel+= 1
    else:    
        countreshka+= 1
    i+= 1         
if countreshka < countorel:
    print(f"Нужно перевернуть {countreshka} монет(ы) 'РЕШКА' на 'ОРЁЛ'")
elif countreshka == countorel:
    print(f"Количество монет 'РЕШКА' и 'ОРЁЛ' равны, что хотите, то и переворачивайте")    
else:
    print(f"Нужно перевернуть {countorel} монет(ы) 'ОРЁЛ' на 'РЕШКА'")           