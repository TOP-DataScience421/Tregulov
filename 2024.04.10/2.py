 
user_input = input("Введите целое число - количество итераций для ввода: ")


try:
    number = int(user_input)
 
    sum_positive = 0
    i = 0

    while i < number:
        user_number = int(input("Введите целое число "))
        
        if user_number > 0:
            sum_positive += user_number
     
        i += 1
     
    print(f"Сумма положительных чисел {sum_positive}")
except ValueError:
    print("Пожалуйста введите целое число")