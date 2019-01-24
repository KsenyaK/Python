x = 4.5
y = 'word'
c = False

x, y, c = (4.5, 'word', False) #так можно?

name = input ('Введите слово ')
print (name)
x = name
print (x)

name = int(input ('Введите число  '))
b = name
print (2 + b)

name = int(input ('Введите свой возраст '))
if name >= 18:
    print ('Доступ разрешен')
else:
    print ('Извините, пользование данным ресурсом только с 18 лет')

#normal

number = int(input('Введите число от 0 до 10 '))
while number <= 0 or number >= 10:
    print ('Число неверное, допустимый диапазон -больше 0, но меньше 10 ')
    number = int(input('Введите число от 0 до 10 '))
if number > 0 or number < 10:
    print (number**2)

    
x = int(input ('Введите любое число x= '))
y = int(input ('Введите другое число y= '))
print('x = ', x)
print('y = ', y)
x, y = y, x
print (x, y)
    
    
    #hard
print ('Медицинская анкета')
a = str(input('Введите имя '))
b = str(input('Введите фамилию '))
x = int(input('Введите возраст '))
y = int(input('Введите вес '))
print (a, b, 'возраст', x, 'вес', y)
if x > 40  and 50 < y > 120:
    print ('вам требуется врачебный осмотр')
elif 30 > x <= 40 and 50 < y > 120:
    print ('Начинайте вести правильный образ жизни')
else:
    print ('Вы пока относительно здоровы')
print ('Диагноз ясен')





