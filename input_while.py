# Implementation of while loop and input functions

# Infinite while loop
while True:
    print("1. Number one")
    print("2. Number two")
    print("3. Break out of infinite loop")
    option = input("Pick an option: ")
    if option == "1":
        print("You chose 1")
    elif option == "2":
        print("You chose 2")
    elif option == "3":
        print("Leaving the loop!")
        break
    else:
        print("Invalid command")
print("You have left the loop.")