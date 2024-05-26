##### MohammadAli Mirzaei #####

# Prompt the user to enter the length of the list
Number = int(input("Enter the length of the list : "))

# Initialize an empty list
lst = []

# Iterate 'Number' times to get input numbers from the user and append them to the list
for i in range(Number):
    lst.append(int(input(f"Enter number {i+1} : ")))

# Reverse the order of elements in the list
lst.reverse()

# Print the reversed list
print(lst)
