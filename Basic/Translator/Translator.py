import gtts  # Importing the 'gtts' library for text-to-speech conversion

def Database():
    global Words_Bank  # Declaring 'Words_Bank' as a global variable
    # Opening and reading the translation database file
    with open("Translator\Translate.txt", "r") as database_translate:
        # Splitting the file content into lines
        Temp = database_translate.read().split("\n")
        Words_Bank = []  # Initializing an empty list to store translation dictionary
        # Iterating through lines to create translation dictionary pairs
        for line in range(0, len(Temp) - 1, 2):
            # Creating a dictionary with "English" and "Persian" keys and adding it to Words_Bank
            Dictionary = {"English": Temp[line], "Persian": Temp[line + 1]}
            Words_Bank.append(Dictionary)

def Show_Menu():
    # Displaying the menu options
    print("1 : Translate English to Persian")
    print("2 : English text to speak")
    print("3 : Translate Persian to English")
    print("4 : Persian text to speak")
    print("5 : Add a new word to the database")
    print("6 : Exit")

def Translate_English_to_Persian():
    User_Text = input("Please enter your English text :  ")  # Prompting user for input
    User_Word = User_Text.split(" ")  # Splitting the input into words
    
    # Iterating through each word in the input text
    for User_Word in User_Word:
        # Searching for the word in the translation database
        for word in Words_Bank:
            if User_Word == word["English"]:
                print(word["Persian"], end=" ")  # Printing the Persian translation
                break
        else:
            print(User_Word, end=" ")  # If word not found, printing the original word
    print("")  # Printing a new line after translation

def English_text_to_speak():
    User_Text = input("Please enter your English text : ")  # Prompting user for input
    sound = gtts.gTTS(User_Text, lang="en", slow=False)  # Generating audio from text
    sound.save("Pylearn7\Assignment 8/voice.mp3")  # Saving the audio file

def translate_Persian_to_English():
    User_Text = input("Please enter your Persian text : ")  # Prompting user for input
    User_Word = User_Text.split(" ")  # Splitting the input into words
    
    # Iterating through each word in the input text
    for User_Word in User_Word:
        # Searching for the word in the translation database
        for word in Words_Bank:
            if User_Word == word["Persian"]:
                print(word["English"], end=" ")  # Printing the English translation
                break
        else:
            print(User_Word, end=" ")  # If word not found, printing the original word
    print("")  # Printing a new line after translation

def Persian_text_to_speak():
    User_Text = input("Please enter your Persian text : ")  # Prompting user for input
    sound = gtts.gTTS(User_Text, lang="ur", slow=False)  # Generating audio from text
    sound.save("Pylearn7\Assignment 8/voice.mp3")  # Saving the audio file

def Add_To_Database():
    # Prompting user to enter new English and Persian text pairs
    user_English_text = input("Please enter your English text : ")
    user_Persian_text = input("Please enter your Persian text : ")
    # Appending the new text pairs to the translation database file
    with open("Pylearn7\Assignment 8\Translate.txt", "a") as database:
        database.write(f"{user_English_text}\n{user_Persian_text}\n")

Database()  # Initializing the translation database

while True:
    Show_Menu()  # Displaying the menu
    choice = int(input("Please enter your option : "))  # Prompting user for menu choice

    # Executing the selected menu option based on user input
    if choice == 1:
        Translate_English_to_Persian()
    elif choice == 2:
        English_text_to_speak()
    elif choice == 3:
        translate_Persian_to_English()
    elif choice == 4:
        Persian_text_to_speak()
    elif choice == 5:
        Add_To_Database()
    elif choice == 6:
        print("GoodBye😘")
        exit(0)  # Exiting the program
