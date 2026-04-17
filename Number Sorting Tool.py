numbers = input("Enter numbers separated by space:")
num_list = list(map(int,numbers.split())) #Convert input into list of integers 
choice = input("Type 'A' fpr Ascending or 'D' for Descending:")
if choice == 'A':
    num_list.sort()
    print("Ascending order:",num_list)
elif choice == 'D':
    num_list.sort(reverse=True)
    print("Descending order:",num_list)
else:
    print("Invalid choice!")
    
