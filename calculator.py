 # Calculator App

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


while True:
    print("\n--- Calculator ---")
    
    try:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
    except:
        print("Invalid input! Please enter numbers.")
        continue

    print("\nChoose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", subtract(a, b))
    elif choice == "3":
        print("Result:", multiply(a, b))
    elif choice == "4":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")

    cont = input("\nDo you want to continue? (yes/no): ")
    if cont.lower() != "yes":
        print("Exiting calculator...")
        break
