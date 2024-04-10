str1 = input("Введите клетку 1 ")
str2 = input("Введите клетку 2 ")


aceg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numb = ['1', '2', '3', '4', '5', '6', '7', '8']

poz_a_1 = aceg.index(str1[0]) + 1
poz_n_1 = numb.index(str1[1]) + 1

poz_a_2 = aceg.index(str2[0]) + 1
poz_n_2 = numb.index(str2[1]) + 1


hod_a = abs(poz_a_1 - poz_a_2)
hod_n = abs(poz_n_1 - poz_n_2)

if hod_a <= 1 and hod_n <= 1:
    print('да')
else:
    print('нет')
    
# Введите клетку 1 h8
# Введите клетку 2 g7
# да

# Введите клетку 1 h8
# Введите клетку 2 a1
# нет