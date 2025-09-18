import random
def get_parity_hint(number):
    if number % 2 == 0:
        return "HINT: The number is even" 
    else:
        return "HINT: The number is odd"

def get_divisibility_hint(number):
    if number % 3 == 0:
        return "HINT: The number is divisible by 3"
    elif number % 5 == 0:
        return "HINT: The number is divisible by 5"
    else:
        return "HINT: The number is NOT divisible by 3 or 5"

def get_range_hint(number, current_min=1, current_max=100):
    return f"HINT: The narrowed range is from {current_min} to {current_max}"

def get_first_digit_hint(number):
    return f"HINT: The first digit of the number is {str(number)[0]}"

def play_game():
    print("เกมทายตัวเลข")
    print("Guess my number between 1 and 100!")
    print("You have unlimited attempts.\n")
    
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        attempts += 1
        try:
            guess = int(input(f"Attempt {attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if guess == random_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

        if attempts == 3:
            print(get_parity_hint(random_number))
        elif attempts == 5:
            print(get_divisibility_hint(random_number))
        elif attempts == 7:
            print(get_range_hint(random_number, max(1, random_number - 25), min(100, random_number + 25)))
        elif attempts == 10:
            print(get_first_digit_hint(random_number))

    print(f"The correct number was: {random_number}")

play_game()
