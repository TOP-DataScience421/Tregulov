user_input = input("Введите натуральное число: ")

try:
    n = int(user_input)        
    
    count_primes = 0

    # Генерируем минимальное и максимальное n-значные числа
    start = 10**(n - 1)
    end = 10**n

    # Перебираем все n-значные числа от start до end-1
    for number in range(start, end):
        is_prime = True
        
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime =  False  # Найден делитель, число не является простым

        if is_prime:
            count_primes += 1  
        
        
    
    print(count_primes)  
    
except ValueError:
    print("Ошибка: введено некорректное значение. Пожалуйста, введите натуральное число.")
    
# Введите натуральное число: 3
# 143

# Введите натуральное число: 5
# 8363