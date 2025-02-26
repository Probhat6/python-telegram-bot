from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests

TOKEN = "YOUR_BOT_TOKEN"

# Function to fetch token data
def get_token_data(token):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    
    if token in data:
        price = data[token]["usd"]
        return f"Token: {token.capitalize()}\nPrice: ${price}"
    else:
        return "Token not found! Please check the name."

# Command handler for token price
def token_price(update: Update, context: CallbackContext):
    if context.args:
        token_name = context.args[0].lower()
        message = get_token_data(token_name)
    else:
        message = "Usage: /price <token_name>"
    
    update.message.reply_text(message)

# Start the bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Command Handler
    dp.add_handler(CommandHandler("price", token_price))

    # Start polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
