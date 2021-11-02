import os
import telebot
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Hello','Hi','HI','namaste'])

def Hello(message):
    bot.reply_to(message,"Hey, this is Proffesor. How are you?")

def main():
    bot.polling()

if __name__ == '__main__':
    main()

