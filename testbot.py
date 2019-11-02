import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
#Need command and message handler as your bot should be able to handle both. 

# When you write funcs: def <functionaname>(update, context). Wont be using context but it's still required
def start(update, context):
    update.message.reply_text("UwU") #takes what you're messaging and reply with UwU

def help(update, context):
    update.message.reply_text("Hewp! :o")

def handle_text(update, context):
    update.message.reply_text(owo.text_to_owo(update.message.text))

def get_joke(update, context):
    """Fetch joke from the web and return."""
    url = 'https://icanhazdadjoke.com/'
    headers = {'Accept': 'application/json'} #constraints on response: receive in json format 
    joke_msg = requests.get(url, headers=headers).json().get('joke') #Converts to dictionary
    update.message.reply_text(joke_msg)

def main():
    updater = Updater("1039349438:AAE1GVzhQzdfZ86jDSGoVQv-K_giw3KXoYs", use_context=True) #define updater, enables use of context

    dp = updater.dispatcher #Updater checks for user updates, Dispatcher checks for updates and sends them to the server

    dp.add_handler(CommandHandler("start", start)) #Wont handle normal text. Associates function with the function name
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("joke", get_joke))
    dp.add_handler(MessageHandler(Filters.text, handle_text))
    updater.start_polling() #Starts looking for updates

    updater.idle() #to stop the bot 


if __name__ == '__main__':
    main() 