"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no
"""
a = int(input('Номер билета: '))
i = 0
sum1 = 0

while i < 3 :
    temp1 = a % 10
    sum1 = sum1 + temp1
    a = a//10
    i+=1
print(f'Сумма последних 3х чисел: {sum1}') 
  
sum2 = 0
while i < 6 :
    temp2 = a % 10
    sum2 = sum2 + temp2
    a = a//10
    i+=1
print(f'Сумма первых 3х чисел: {sum2}')   

if sum1 == sum2 :
    print('***Билет счастливый***')
else :
    print('***Билет не счастливый***')