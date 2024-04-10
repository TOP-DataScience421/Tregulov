str1 = input('Введите шахматную клетку 1: ')
str2 = input('Введите шахматную клетку 2: ')


#a, с, e, g - четные белые, не четные черные
#b, d, f, h - четные черные, не четные белые

aceg = ('a', 'c', 'e', 'g')

color1 = ''


if str1[0] in aceg:
    if (int(str1[1]) + 1) % 2 == 0:
        color1 = 'w'
    else:   
        color1 = 'b'
else:
    if (int(str1[1]) + 1) % 2 == 0:
        color1 = 'b'
    else:   
        color1 = 'w'
        

color2 = ''

if str2[0] in aceg:
    if (int(str2[1]) +1) % 2 == 0:
        color2 = 'w'
    else:   
        color2color2 = 'b'
else:
    if (int(str2[1]) + 1) % 2 == 0:
        color2 = 'b'
    else:   
        color2 = 'w'
        
if color1 == color2:
    print('да')
else:
    print('нет')


# Введите шахматную клетку 1: a3
# Введите шахматную клетку 2: g3
# да

# Введите шахматную клетку 1: a3
# Введите шахматную клетку 2: b1
# нет