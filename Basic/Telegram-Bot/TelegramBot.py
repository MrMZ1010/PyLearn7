##### Mohammad Ali Mirzaei #####

import random
import datetime
from persiantools import jdatetime
import qrcode
import gtts
import telebot
from telebot import types

# Initialize the Telegram bot with the provided token
bot = telebot.TeleBot("YOUR_TELEGRAM_BOT_TOKEN_HERE", parse_mode=None)

# Create a custom keyboard layout
markup = telebot.types.ReplyKeyboardMarkup(row_width=3)

# Define keyboard buttons for each option
item_markup1 = telebot.types.KeyboardButton("Game")
item_markup2 = telebot.types.KeyboardButton("Age")
item_markup3 = telebot.types.KeyboardButton("Voice")
item_markup4 = telebot.types.KeyboardButton("Max")
item_markup5 = telebot.types.KeyboardButton("Argmax")
item_markup6 = telebot.types.KeyboardButton("QRcode")
item_markup7 = telebot.types.KeyboardButton("Help")

# Add buttons to the custom keyboard layout
markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)

# Handle the /start command to welcome users and display the custom keyboard layout
@bot.message_handler(commands=["start"])
def send_welcome(message):
    user_name = message.from_user.first_name
    bot.reply_to(message, f" Welcome, {user_name} 🌹", reply_markup=markup)

# Handle all incoming messages
@bot.message_handler(func=lambda m: True)
def Main_Func(message):
    if message.text == "Game":
        Start_Game(message)
    elif message.text == "New game":
        New_Game(message)
    elif message.text == "Home":
        Home(message)
    elif message.text == "Age":
        Get_Birthday(message)
    elif message.text == "Voice":
        Voice_Text(message)
    elif message.text == "Max":
        Get_Numbers(message)
    elif message.text == "Argmax":
        Get_Numbers_2(message)
    elif message.text == "QRcode":
        QRCode_Text(message)
    elif message.text == "Help":
        Help(message)

# Initialize variables for the game
Number = random.randint(1, 100)
chat_id = None
Counter = 0

# Display the home screen
def Home(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
    item_markup1 = telebot.types.KeyboardButton("Game")
    item_markup2 = telebot.types.KeyboardButton("Age")
    item_markup3 = telebot.types.KeyboardButton("Voice")
    item_markup4 = telebot.types.KeyboardButton("Max")
    item_markup5 = telebot.types.KeyboardButton("Argmax")
    item_markup6 = telebot.types.KeyboardButton("QRcode")
    item_markup7 = telebot.types.KeyboardButton("Help")
    markup.add(item_markup1, item_markup2, item_markup3, item_markup4, item_markup5, item_markup6, item_markup7)
    lst = ["Alright", "OK", "Okay", "Fair enough", "Sure"]
    bot.reply_to(message, random.choice(lst), reply_markup=markup)

# Start the number guessing game
def Start_Game(message):
    global chat_id
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup(row_width=1)
    item_markup1 = types.KeyboardButton("New game")
    item_markup2 = types.KeyboardButton("Home")
    markup.add(item_markup1)
    markup.add(item_markup2)
    msg = bot.send_message(chat_id, "Guess a Number between 1 to 100", reply_markup=markup)
    bot.register_next_step_handler(msg, Guess_Number)

# Handle user's guesses in the number guessing game
def Guess_Number(message):
    global Number
    global Counter
    if message.text == "Home":
        Home(message)
    elif message.text == "New game":
        New_Game(message)
    else:
        guess = int(message.text)
        if guess > Number:
            Counter += 1
            msg = bot.send_message(chat_id, "Go down 🔽")
            bot.register_next_step_handler(msg, Guess_Number)
        elif guess < Number:
            Counter += 1
            msg = bot.send_message(chat_id, "Go up 🔼")
            bot.register_next_step_handler(msg, Guess_Number)
        elif guess == Number:
            bot.send_message(chat_id, f"That is correct ✅ | you`ve had {Counter + 1} guesses ")
            Counter = 0

# Start a new game
def New_Game(message):
    global Counter
    global Number
    Number = random.randint(1, 100)
    msg = bot.send_message(chat_id, "Guess a Number between 1 to 100")
    bot.register_next_step_handler(msg, Guess_Number)

# Get the user's birthday and calculate their age
def Get_Birthday(message):
    msg = bot.send_message(message.chat.id, "Please give me your birthday in Solar year like this 1365-06-16")
    bot.register_next_step_handler(msg, Calculate_Age)

def Calculate_Age(message):
    birthday_year, birthday_month, birthday_day = map(int, message.text.split("-"))
    miladi_date = jdatetime.JalaliDate(birthday_year, birthday_month, birthday_day).to_gregorian()
    age_timedelta = datetime.date.today() - miladi_date
    age_years = age_timedelta.days // 365
    bot.send_message(message.chat.id, f"You are {age_years} years old")

# Convert text to speech
def Voice_Text(message):
    msg = bot.send_message(message.chat.id, "Please give me an English text")
    bot.register_next_step_handler(msg, Text_To_Voice)

def Text_To_Voice(message):
    user_text = message.text
    voice = gtts.gTTS(user_text, lang="en", slow=False)
    voice.save("voice.mp3")
    with open("voice.mp3", "rb") as voice_file:
        bot.send_voice(message.chat.id, voice_file)

# Get a list of numbers and return the maximum number
def Get_Numbers(message):
    msg = bot.send_message(message.chat.id, "Please give me a list of numbers like this 14,7,78,15,8,19,20")
    bot.register_next_step_handler(msg, Show_Max)

def Show_Max(message):
    Numbers = list(map(int, message.text.split(",")))
    Max_Number = max(Numbers)
    bot.send_message(message.chat.id, f"The maximum number is {Max_Number}")

# Get a list of numbers and return the index of the maximum number
def Get_Numbers_2(message):
    msg = bot.send_message(message.chat.id, "Please give me a list of numbers like this 14,7,78,15,8,19,20")
    bot.register_next_step_handler(msg, Show_Max_Arg)

def Show_Max_Arg(message):
    Numbers = list(map(int, message.text.split(",")))
    Max_Index = Numbers.index(max(Numbers))
    bot.send_message(message.chat.id, f"Maximum number index is {Max_Index}")

# Generate a QR code from text
def QRCode_Text(message):
    msg = bot.send_message(message.chat.id, "Please give me your text")
    bot.register_next_step_handler(msg, Create_QRCode)

def Create_QRCode(message):
    qr_img = qrcode
