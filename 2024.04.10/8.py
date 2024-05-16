
n = int(input("Введите число: "))
    
if n <= 0:
    fib_numbers = []

elif (n == 1): 
    fib_numbers = [1]
    
else:
    fib_numbers = [1, 1]
    for i in range(2, n):
        next_number = fib_numbers[-1] + fib_numbers[-2]
        fib_numbers.append(next_number)    
     

print(" ".join(map(str, fib_numbers)))


# Введите число: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597