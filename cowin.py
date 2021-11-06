import requests
import sys
from datetime import datetime

base_cowin_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
now = datetime.now()
today_date = now.strftime("%d-%m-%Y")
api_url_telegram = "https://api.telegram.org/bot2039610624:AAFKOD48lPhrnBw5mbABeHQG6cU_xxLI7s0/sendMessage?chat_id=@__groupid__&text="
group_id = "cowin_python"

pincode = sys.argv[1]

def fetch_data_from_cowin(pincode):
    query_params = "?pincode={}&date={}".format(pincode, today_date)
    final_url = base_cowin_url+query_params
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
    response = requests.get(final_url,headers=hdr)
    extract_availability_data(response)
    #print(response.text)

# def fetch_data_for_state(district_ids):
#     for district_id in district_ids:
#         fetch_data_from_cowin(district_id)

def extract_availability_data(response):
    response_json = response.json()
    for center in response_json["centers"]:
        for session in center["sessions"]:
            if session["available_capacity_dose1"] > 0:
                message = "CenterId: {}, Name: {}, Dose 1 Slots: {}, Dose 2 Slots:{}, Vaccine name: {}, Minimum Age: {}".format(
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
    print(response)




if __name__=="__main__":    
    fetch_data_from_cowin(pincode)