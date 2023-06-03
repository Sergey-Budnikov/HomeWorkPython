"""
Задача №29. Решение в группах
Ваня и Петя поспорили, кто быстрее решит 
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем (число 0 не входит в
последовательность)”. Однако 2 друга оказались не 
такими смышлеными. Никто из ребят не смог до 
конца сделать это задание. Они решили так: у кого 
будет меньше ошибок в коде, тот и выиграл спор. За 
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих 
слайдах
"""
num = maxnum = int(input("Введите число: "))
while num != 0:
    num = int(input("Введите число: ")) 
    if num > maxnum:
        maxnum = num 
    # значение тру if  (условие)   else значение элс 
    # maxnum = num if num > maxnum else maxnum - другая запись строк 20 и 21 через тернарный оператор.       
print(f"Максимальный элемент: {maxnum}")    