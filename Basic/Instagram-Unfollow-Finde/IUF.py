##### MohammadAli Mirzaei #####

# Import necessary modules
import instaloader
from getpass import getpass

# Open the file containing old followers in read mode and read each line into a list
file = open("followers.txt", "r")
Old_Followers = []
for line in file:
    Old_Followers.append(line)
file.close()

# Initialize an Instaloader instance
Loader = instaloader.Instaloader()

# Prompt the user to enter their Instagram username and password
Username = input("Enter your username: ")
Password = getpass("Enter your password: ")

# Login to Instagram using the provided username and password
Loader.login(Username, Password)
print("Login was successful✅")

# Get the profile of the Instagram user "MrMZ1010"
Profile = instaloader.Profile.from_username(Loader.context, "MrMZ1010")

# Create an empty list to store new followers
New_Followers = []

# Iterate over the followers of the profile and append them to the list of new followers
for follower in Profile.get_followers():
    New_Followers.append(follower)

# Iterate over the new followers and print those who are not in the list of old followers
for new in New_Followers:
    if new not in Old_Followers:
        print(new)

# Open the file in write mode to update the list of followers
f = open("followers.txt", "w")

# Write each new follower to the file
for follower in New_Followers:
    f.write(follower + "\n")

# Close the file
f.close()


f.close()
