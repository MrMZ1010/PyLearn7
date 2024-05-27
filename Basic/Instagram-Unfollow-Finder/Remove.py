##### MohammadAli Mirzaei #####

# Prompt the user to enter the length of the list
Number = int(input("Enter the length of the list : "))

# Initialize an empty list
lst = []

# Iterate 'Number' times to get input numbers from the user and append them to the list
for i in range(Number):
    lst.append(int(input(f"Enter number {i+1} : ")))

# Iterate over each number in the list
for number in lst:
    # Check if the count of the current number in the list is greater than 1
    if lst.count(number) > 1:
        # If the count is greater than 1, remove the first occurrence of the number from the list
        lst.remove(number)

# Print the modified list with duplicates removed
print(lst)

