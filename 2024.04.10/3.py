user_input = input("Введите натуральное число: ")

try:
    n = int(user_input)  
    
    sum_divisors = 0
    
    if n > 0:
        for i in range(1, n + 1):
            if n % i == 0:
                sum_divisors += i  
    

    print(sum_divisors)  
except ValueError:
    print("Ошибка: введено некорректное значение. Пожалуйста, введите натуральное число.")
    
# Введите натуральное число: 50
# 93