##### Mohammad Ali Mirzaei #####

import qrcode

User_Name = input("Enter your name : ")
User_Phone = input("Enter your phone number : ")

img = qrcode.make(f"{User_Name} | {User_Phone}")
img.save("QRcode.png")