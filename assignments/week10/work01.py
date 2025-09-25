print('=== PERSONAL INFORMATION VALIDATOR ===')

name = input('Enter your name: ')
age = int(input('Enter your age: '))
phone = input('Enter your phone number: ')

name_validator = True
for char in name:
    if not (char.isalpha() or char == " "):
        name_validator = False
        break

age_validator = 18 <= age <= 30
phone_validator = len(phone) == 10 and phone.isdigit()

print('\nValidation Results:')
if name_validator:
    print('Name: Valid (contains only letters and spaces)')
else:
    print('Name: Invalid (only letters and spaces are allowed)')

if age_validator:
    print(f'Age: Valid ({age} years old)')
else:
    print(f'Age: Invalid ({age} years old - must be 18 to 30)')

if phone_validator:
    print('Phone: Valid (10-digit number)')
else:
    print('Phone: Invalid (must be a 10-digit number)')

print('\nFormatted Information:')
print('Name:', name.upper())

if 18 <= age <= 30:
    print('Group: Young Adult (18-30)')
elif 30 < age <= 65:
    print('Group: Adult (31-65)')
else:
    print('Group: Not in allowed range')

print(f'Phone: +66-{phone}')
