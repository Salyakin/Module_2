from time import sleep
name = input('Напишите пожалуйста ваше имя: ')
if name == 'Ivan':
    print ('Здравствуйте, ', name)
else:
    print ('Привет')
first = int (input('Введите челое число: '))
second = int (input('Введите челое число: '))
third = int (input('Введите челое число: '))
if first == second == third:
    print ('Введенные вами числа равны между собой: ',3)
elif first == second or first == third or second == third:
    print ('Равны между собой только два числа из трех введенных: ',2)
else:
    print ('Ваши числа не равны',0)
sleep(3)
print ('Вы молодец')
