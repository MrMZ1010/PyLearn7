##### Mohammad Ali Mirzaei #####

import instaloader
from getpass import getpass

file = open("followers.txt", "r")
Old_Followers = []
for line in file:
    Old_Followers.append(line)
file.close()

Loader = instaloader.Instaloader ()

Username = input("Enter your username: ")
Password = getpass("Enter your password: ")

Loader.login(Username, Password)
print("Login was successful✅")

Profile = instaloader.Profile.from_username(Loader.context, "MohammadAli_Mirzaei")

New_Followers = []
for follower in Profile.get_followers():
    New_Followers.append(follower)

for new in New_Followers :
    if new  not in Old_Followers:
        print(new)


f = open("followers.txt", "w")
for follower in New_Followers:
    f.write(follower + "\n")

f.close()
