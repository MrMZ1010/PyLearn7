import gtts

def Database():
    global Words_Bank
    with open("Pylearn7\Assignment 8\Translate.txt","r") as database_translate:
        Temp = database_translate.read().split("\n")
        Words_Bank = []
        for line in range(0,len(Temp) - 1,2):
            Dictionary = {"English":Temp[line],"Persian":Temp[line+1]}
            Words_Bank.append(Dictionary)

def Show_Menu():
    print("1 : Translate Eglish to Persian")
    print("2 : English text to speak")
    print("3 : Translate Persian to English ")
    print("4 : Persian text to speak ")
    print("5 : Add a new word to the database")
    print("6 : Exit ")

def Translate_English_to_Persian():
    User_Text = input("Please enter your English text :  ")
    User_Word = User_Text.split(" ")
    
    for User_Word in User_Word:
        for word in Words_Bank:
            if User_Word == word["English"]:
                print(word["Persian"],end=" ")
                break
        else:
            print(User_Word,end=" ")
    print("")

def English_text_to_speak():
    User_Text = input("Please enter your English text : ")
    sound = gtts.gTTS(User_Text,lang="en",slow=False)
    sound.save("Pylearn7\Assignment 8/voice.mp3")

def translate_Persian_to_English():
    User_Text = input("Please enter your Persian text : ")
    User_Word = User_Text.split(" ")
    
    for User_Word in User_Word:
        for word in Words_Bank:
            if User_Word == word["Persian"]:
                print(word["English"],end=" ")
                break
        else:
            print(User_Word,end=" ")
    print("")

def Persian_text_to_speak():
    User_Text = input("Please enter your Persian text : ")
    sound = gtts.gTTS(User_Text,lang="ur",slow=False)
    sound.save("Pylearn7\Assignment 8/voice.mp3")

def Add_To_Database():
    user_English_text = input("Please enter your English text : ")
    user_Persian_text = input("Please enter your Persian text : ")
    with open("Pylearn7\Assignment 8\Translate.txt", "a") as database:
        database.write(f"{user_English_text}\n{user_Persian_text}\n")

Database()

while True:
    Show_Menu()
    choice = int(input("Please enter your option : "))

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
        exit(0)
