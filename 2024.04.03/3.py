number1 = int(input('введите год: '))

if number1 % 4 == 0 and number1 % 100 != 0:
    print("да")
else:
    print("нет")
    
# введите год: 1764
# да    

# введите год: 1765
# нет