number1 = int(input('введите число 1: '))
number2 = int(input('введите число 2: '))

ost = number1%number2

if ost == 0:
    print(f"{number1} делится на {number2} нацело")
    print(f"частное {number1/number2} ") 
else:
    print(f"{number1} не делится на {number2} нацело")
    print(f"неполное частное {(number1/number2):.0f}")  
    print(f"остаток {ost}")     

# введите число 1: 10
# введите число 2: 5
# 10 делится на 5 нацело
# частное 2.0

# введите число 1: 9
# введите число 2: 2
# 9 не делится на 2 нацело
# неполное частное 4
# остаток 1