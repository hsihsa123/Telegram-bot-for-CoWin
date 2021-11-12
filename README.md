# Telegram-bot-for-cowin-appointment

REQUIREMENTS:

IMPORT FOLLOWING MODULES:
1. python-dotenv
2. requests

CREATE TELEGRAM BOT:
1. Enter @Botfather in the search tab and choose this bot.
2. Write /start to start the bot.
3. Choose or type the /newbot command and send it.
4. Choose a name for your bot — your subscribers will see it in the conversation. And choose a username for your bot — the bot can be found by its username in searches. The username must be unique and end with the word “bot.”
5. After you choose a suitable name for your bot — the bot is created. You will receive a message with a link to your bot t.me/<bot_username>, recommendations to set up a profile picture, description, and a list of commands to manage your new bot.
6. Copy your token value and save it securely as it will needed in the python script.


The Python script has the following main steps :

1.  Ping the co-win API & fetch data
    Cowin API's can be found here : https://apisetu.gov.in/api/cowin
    
    The above python script is fetching data from pincodes as reference, but the same can be modified as per the need of the user. There are various different API's     present in the above link. 
   
 2. Extract the information we want from the API's.
 3. Push message to telegram group whenever there is availability.     
 
 USAGE OF THE SCRIPT:
 Run the python program and go to telegram group mentioned in the code.
Type for any pincode with a "/" as a prefix and the bot will automatically send all the slots availability in that area.
    




