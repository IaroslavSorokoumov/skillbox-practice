##
##player = int(input('Кубик Кости: '))
##owner = int(input('Кубик владельца: '))
##if player >= owner: # сравнение кубиков, если у Кости больше, то он платит
##  print('Сумма:', player - owner)
##  print('Игрок платит')
##else:
##  print('Сумма:', player + owner)
##  print('Владелец платит')
##print('Игра окончена')
##  

##hours = int(input('Введите отработанные часы: '))
##loan = int(input('Введите остаток по кредиту: '))
##money = int(input('Введите траты на еду: '))
##sal = 200 * hours/2**3 + hours # расчёт з/п
##expen = loan + money  # расчёт расходов
##if sal >= expen:
##  print('Часов хватает. Можно отдохнуть')
##else:
##  print('Часов не хватает. Придётся работать больше')
##print('Зарплата:', sal)

##a = int(input('Введите первое число: '))
##b = int(input('Введите второе число: '))
##c = int(input('Введите третье число: '))
##if a > b > c:
##  print('Наибольшее число:', a)
##if b > a > c:
##  print('Наибольшее число:', b)
##else:
##  print('Наибольшее число:', c)

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))
num_3 = int(input('Введите третье число: '))

if num_1 > num_2:
  maximum = num_1
else:
  maximum = num_2
if maximum < num_3:
  maximum = num_3

print('Наибольшее число:', maximum)
