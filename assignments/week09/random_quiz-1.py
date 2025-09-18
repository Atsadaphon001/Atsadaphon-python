import random

def test_random():
    random_number = random.randint(1, 20)
    attempts = 6
    
    for num in range(attempts):
        print(f'รอบที่ {num+1} เเล้วนะเว้ย')
        number = int(input(f'input number {num+1}/6 = '))
        if number == random_number:
            print('you win เก่งวะๆ')
            break
        elif number > random_number:
            print('Too high')
        else:
            print('Too low')
    else:
        print('You lose กากวะๆ')
    print(f'Number Win is : {random_number} ')

test_random()
