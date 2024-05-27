##### MohammadAli Mirzaei #####

# Import the qrcode module
import qrcode

# Prompt the user to enter their name and phone number
User_Name = input("Enter your name : ")
User_Phone = input("Enter your phone number : ")

# Generate a QR code containing the user's name and phone number
# Using f-string to format the string with user's name and phone number
img = qrcode.make(f"{User_Name} | {User_Phone}")

# Save the generated QR code as an image file named "QRcode.png"
img.save("QRcode.png")
