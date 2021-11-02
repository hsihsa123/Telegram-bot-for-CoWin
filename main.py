import os
import telebot
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Hello','Hi','HI','namaste'])

def Hello(message):
    bot.send_message(message.chat.id,"Hey, this is Proffesor. How are you?")

@bot.message_handler(func=lambda m: True)
def repeat(message):
    bot.send_message(message.chat.id, message.text)
    

def main():
    bot.polling()

if __name__ == '__main__':
    main()

