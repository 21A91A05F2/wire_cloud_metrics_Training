from calculations import add
from calculations import subtract
from calculations import multiply
from calculations import divide





while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Choose an Operator (1-5): ")

    if choice == '5':
        print("Exiting the calculator, Goodbye!")
        break

    if choice in['1', '2', '3', '4']:
        num1 = float(input("Enter the First Number: "))
        num2 = float(input("Enter the secound number: "))


        if choice == '1':
            print("Result:", add(num1,num2)) 
        elif choice == '2':
            print("Result:", subtract(num1,num2))
        elif choice == '3':
            print("Result:", multiply(num1,num2))
        elif choice == '4':
            print("Result:", divide(num1,num2))  
    else:
        print("Invalid input! Please Enter a number between 1 and 5.")             
