##### MohammadAli Mirzaei #####

# Prompt the user to enter the length of the list and convert it to an integer
Number = int(input("Enter the length of your list : "))

# Initialize an empty list to store numbers entered by the user
Numbers_List = []

# Iterate from 0 to the entered number
for i in range(Number):
    # Prompt the user to enter a number and add it to the Numbers_List
    Numbers_List.append(int(input(f"Enter the number {i + 1} : ")))

# Check if the Numbers_List is equal to its sorted version
if Numbers_List == sorted(Numbers_List):
    # If the Numbers_List is equal to its sorted version, print a message indicating that the list is sorted
    print("Your list is sorted ")
else:
    # If the Numbers_List is not equal to its sorted version, print a message indicating that the list is not sorted
    print("Your list is not sorted")

