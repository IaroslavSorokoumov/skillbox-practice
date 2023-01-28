##
##year = 2018
##speeds = 24
##bike_year = int(input('Укажите год выпуска велосипеда: '))
##bike_speeds = int(input('Укажите кол-во скоростей: '))
##
##if bike_year >= year and bike_speeds >= speeds:
##  print('Подходящий вариант.')
##else:
##  print('Не соответствует критериям выбора.')


##year = 2018
##speeds = 24
##bike_year = int(input('Укажите год выпуска велосипеда: '))
##bike_speeds = int(input('Укажите кол-во скоростей: '))
##
##if bike_year < year or bike_speeds < speeds:
##  print('Не соответствует критериям выбора.')
##
##else:
##  print('Подходящий вариант.')

##points = 280
##medal = 1
##
##ab_points = int(input('Укажите количество баллов: '))
##medal_state = int(input('Есть ли у вас золотая медаль? '))
##
##if ab_points < points or medal_state != medal:
##  print('К сожалению Вы не проходите по критериям постуления в ВУЗ')
##else:
##  print('Вы приняты!')

low_temprt = 0
high_temprt = 100
temprt = int(input('Введите температуру среды: '))

if low_temprt <= temprt and high_temprt >= temprt:
  print('Температура воды в нужном диапазоне')
else:
  print('Температура воды вышла за безопасный диапазон!')
