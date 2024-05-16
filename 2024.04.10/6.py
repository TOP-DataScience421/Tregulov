ticket_number = input("Введите номер билета:")
    

if len(ticket_number) == 6:

    first_half = ticket_number[:3]
    second_half = ticket_number[3:]

    try:
        first_sum = sum(int(digit) for digit in first_half)
        second_sum = sum(int(digit) for digit in second_half)
            
        if first_sum == second_sum:
            print("Билет счастливый")
        else:
            print("Билет несчастливый")
    except ValueError:
        print("Не удалось разобрать билет")
        
        
# Введите номер билета:321123
# Билет счастливый        

# Введите номер билета:123456
# Билет несчастливый
    
