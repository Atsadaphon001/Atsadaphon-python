def welcome_message(name, course):
    return f"Welcome {name} to {course} class!"

name = input("Enter your name: ")
course = input("Enter your course: ")
print(welcome_message(name, course))

print('\n\n')

def calculate_circle(radius):
    pi = 3.14159
    area = round(pi * radius ** 2, 2)
    circumference = round(2 * pi * radius, 2)
    return {"area": area, "circumference": circumference}
radius = float(input("input radius: "))
print(calculate_circle(radius))

print('\n\n')

def create_user_profile(username, age=18, premium=False):
    if premium:
        return username + " (age: " + str(age) + ") - Premium User"
    else:
        return username + " (age: " + str(age) + ") - Standard User"

print('\n\n')

def analyze_scores(scores):
    total = sum(scores)
    count = len(scores)
    average = total / count
    lowest = min(scores)
    highest = max(scores)
    passed = 0
    for score in scores:
        if scores >=70:
            passed +=1
            
    return {
        'total' : total,
        'average':average,
        'lowest':lowest,
        'highest':highest,
        'passed': passed 
    }

print('\n\n')

def count_vowels_consonants(text):
    text = text.replace(" "," ")
    text = text.lower()
    vowels = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    number = text.count('1') + text.count('2') + text.count('3') + text.count('4') +text.count('5') + text.count('6') + text.count('7') + text.count('8') + text.count('9')
    consonants = len(text) - vowels - number
    return {
        'vowele':vowels,
        'consonants' : consonants
    }