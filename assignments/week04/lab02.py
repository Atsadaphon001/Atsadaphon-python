def number_operations():
    numbers = []
    
    print("Enter 10 numbers:")
    for i in range(10):
        num = int(input(f"Number {i+1}: "))
        numbers.append(num)

    while True:
        print("\nMenu:")
        print("1. Display the original list")
        print("2. List of odd/even numbers")
        print("3. List of numbers greater than the average")
        print("4. Show statistics (sum, average, min, max)")
        print("5. Exit")

        operation = input("Input number option (1-5): ")

        if operation == '1':
            print("Original list:", numbers)

        elif operation == '2':
            for i in numbers:
                if i % 2 == 0:
                    print(f"{i} is even")
                else:
                    print(f"{i} is odd")

        elif operation == '3':
            total = sum(numbers)
            count = len(numbers)
            avg = total / count
            print(f"Average is {avg}")

            greater_than_avg = []
            for n in numbers:
                if n > avg:
                    greater_than_avg.append(n)

            print("Numbers greater than average:")
            for n in greater_than_avg:
                print(n)

        elif operation == '4':
            total = sum(numbers)
            avg = total / len(numbers)
            minimum = min(numbers)
            maximum = max(numbers)
            
            print("Statistics:")
            print(f"Sum: {total}")
            print(f"Average: {avg}")
            print(f"Min: {minimum}")
            print(f"Max: {maximum}")

        elif operation == '5':
            print("Exit")
            break
        
        else:
            print("None")
number_operations()
