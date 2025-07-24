balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        # Complete the menu logic here
        # Your code here:
        if choice == '1':
            print(f'Remaining Balance :{balance}')
            
        elif choice =='2':
            withdraw = float(input('Enter quantity : '))
            if withdraw > balance:
                print("Insufficient funds.")
            else:
                balance = balance - withdraw
                print(f'Remaining Balance :{balance}')

        elif choice == '3':
            deposit = float(input('want to deposit money : '))
            balance = balance+deposit
            print(f'you deposit money :{deposit}')

        elif choice == '4':
            break
        else:
            print ('error')
else:
    print("Invalid PIN")