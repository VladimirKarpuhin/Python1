n = int(input('Введите трёхзначное число: '))
summ = n%10
n = n // 10
summ = summ + n%10
n = n // 10
summ = summ + n%10
print(f'Сумма цифр вашего числа равна: {summ}')