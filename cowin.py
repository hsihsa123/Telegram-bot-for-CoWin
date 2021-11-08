import requests
import telebot
import sys
import os
from datetime import datetime
from dotenv import load_dotenv
from telebot.util import split_string

load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

   
base_cowin_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
now = datetime.now()
today_date = now.strftime("%d-%m-%Y")
api_url_telegram = "https://api.telegram.org/bot{}/sendMessage?chat_id=@__groupid__&text=".format(API_KEY)
group_id = "cowin_python"


def fetch_data_from_cowin(pincode):
    query_params = "?pincode={}&date={}".format(pincode[1:], today_date)
    final_url = base_cowin_url+query_params
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    response = requests.get(final_url,headers=hdr)
    return extract_availability_data(response)
    
def extract_availability_data(response):
    response_json = response.json()
    for center in response_json["centers"]:
        for session in center["sessions"]:
            if session["available_capacity_dose1"] > 0:
                message = " CenterId: {}, \n Name: {}, \n Dose 1 Slots: {}, \n Dose 2 Slots:{}, \n Vaccine name: {}, \n Minimum Age: {} \n ------------------------------------ \n ".format(
                    center["center_id"],center["name"],
                    session["available_capacity_dose1"],
                    session["available_capacity_dose2"],
                    session["vaccine"],
                    session["min_age_limit"]
                )
                send_message_telegram(message)
            else:
                message = "No Slots Available"    

def send_message_telegram(message):
    final_telegram_url = api_url_telegram.replace("__groupid__", group_id)
    final_telegram_url = final_telegram_url + message
    response = requests.get(final_telegram_url)
    

@bot.message_handler(commands=["Hi","Hello","Hey"])
def Welcome(message):
    bot.send_message(message.chat.id,"Hey There, This is Mr. Proffersor, Please type your area pincode with '/' prefix to know the cowin slot availability in your area.")

@bot.message_handler()    
def start(message):
    fetch_data_from_cowin(message.text)
    

if __name__=="__main__":
    bot.polling()
    