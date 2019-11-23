# Сумма и произведение цифр трехзначного числа

NUMBER = int(input('Введите трехзначное целое цисло: '))
MULTIPLICATION = (NUMBER % 10) * (NUMBER // 10 % 10) * (NUMBER // 100)
SUM = (NUMBER % 10) + (NUMBER // 10 % 10) + (NUMBER // 100)

print(f'Произведение цифр трехзначного числа равно: {MULTIPLICATION} '
      f'\nСумма цифр трехзначного числа равна: {SUM}')
