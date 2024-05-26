##### MohammadAli Mirzaei #####

# Take user input for the number of seconds
Seconds = int(input("Enter the seconds : "))

# Calculate the number of hours
Hours = Seconds // 3600

# Calculate the remaining seconds after subtracting the hours
# and then find the number of minutes from those remaining seconds
Minutes = (Seconds % 3600) // 60

# Calculate the remaining seconds after subtracting the hours and minutes
Seconds = Seconds % 60

# Print the result in the format HH:MM:SS
print(f"Result : {int(Hours)}:{int(Minutes)}:{int(Seconds)}")
