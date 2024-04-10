number_sum = 0

number = input('введите число 1: ')

try:
    number = float(number)
except ValueError:
    print('Используйте только цифры')
else:
    if number > 0:
        number_sum = number_sum + number   
        
        
number = input('введите число 2: ')

try:
    number = float(number)
except ValueError:
    print('Используйте только цифры')
else:
    if number > 0:
        number_sum = number_sum + number   
        
number = input('введите число 3: ')

try:
    number = float(number)
except ValueError:
    print('Используйте только цифры')
else:
    if number > 0:
        number_sum = number_sum + number           

print(number_sum)

# введите число 1: 1
# введите число 2: -2
# введите число 3: 5
# 6.0