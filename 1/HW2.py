#ex1
name = 'Test'
str = f'Word {name}, has  {(len(name))}  letters'
print(str)

#ex2
age = input('Enter your age: ')
if not age.isnumeric():
    print('Enter numeric')
elif int(age) > 100:
    print('Enter correct age')
else:
    if int(age) <= 7:
        print('Where are your parents?')
    elif age.find('7') >= 0:
        print('You will be lucky today!')
    elif int(age) <= 16:
        print('This is a movie for adults!')
    elif int(age) >= 65:
        print('Show your pension certificate!')

    else:
        print('And there are no more tickets!')









