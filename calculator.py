import os

again = "Y"

while again == "Y":
    os.system('cls')
    
    print("Simple Calculator")

    print("\nChoose an opearation:")

    print("1: ADDITION")
    print("2: SUBTRACTION")
    print("3: MULTIPLICATION")
    print("4: DIVISION\n")

    choice = int(input("> "))

    x = int(input("\nEnter the first number: "))
    y = int(input("Enter the second number: "))

    if choice == 1:
        print(x+y)
    elif choice == 2:
        print(x-y)
    elif choice == 3:
        print(x*y)
    elif choice == 4:
        print(x/y)
    
    print("Do you want to try again? Y/N ")
    again = input("> ").upper()
    