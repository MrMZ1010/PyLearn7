##### MohammadAli Mirzaei #####

# Prompt the user to enter a string and store it in the variable 'User'
User = input("Enter : ")

# Split the string stored in 'User' into a list of substrings using the space character (" ") as the delimiter,
# and then calculate the length of the resulting list.
# Finally, print the length of the list, which represents the number of words entered by the user.
print(len(User.split(" ")))
