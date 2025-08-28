
while True:
    age = int(input('your age = '))
    if age <13:
        print('child')
    elif 13 <= age <= 19:
        print('teenager')
    elif 20 <= age <= 59:
        print('adult')
    elif age >= 60:
        print('senior')
    else:
        print('none')
    
print(f'your is :{age} ')