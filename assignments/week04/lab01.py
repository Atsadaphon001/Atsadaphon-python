def personal_info_manager():
    person = ("K",19, "Thailand", "bangkok")  
    hobbies = ['sleep','play game','manhwa']

while True:   
    print('1.Display all information,2.Add new hobbies,3.Remove hobbies,4.Update age')
    choice = input("Input option: ")
    if choice == "1":
        print("Name: ", person[0])
        print("Age: ", person[1])
        print("City: ", person[2])
        print("Country: ", person[3])
        print("Hobbies: ", hobbies)
            
    if choice == "2":
        add_hobbies = input("Insert new hobbies : ")
        hobbies.append(add_hobbies)
            
    elif choice == "3":
        del hobbies[0]
            
    elif choice == "4":
        age = int(input("Insert new age: "))
        person_list = list(person)
        person_list[1] = age
        person = tuple(person_list)
            
    elif choice == "5":
        break
        
    else :
        print("Error")