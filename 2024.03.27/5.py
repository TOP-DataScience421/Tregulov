milli_num = int(input("Введите целое значение мили "))
milli_den = int(input("Введите дробное значение мили  "))

km = (milli_num+(milli_den/10))*1.61


print(f"{milli_num}.{milli_den} миль = {round(km, ndigits=1)} ")

# Введите целое значение мили 2
# Введите дробное значение мили  2
# 2.2 миль = 3.5