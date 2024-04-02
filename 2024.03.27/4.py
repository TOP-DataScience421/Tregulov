number_user = int(input("Введите целое трехзначное число "))

number = number_user % 10
number_user = number_user//10

number_10 = number_user % 10
number_user = number_user//10

number_100 = number_user % 10


print(f"Сумма цифр {number_100 + number_10 + number}")
print(f"Произведение цифр {number_100 * number_10 * number}")

# Введите целое трехзначное число 145
# Сумма цифр 10
# Произведение цифр 20