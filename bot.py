import telebot
import requests
import os

# replace YOUR_BOT_TOKEN with your actual bot token obtained from BotFather
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the image bot! Please enter a number to check for an image.")

@bot.message_handler(func=lambda message: True)
def check_image(message):
    num = message.text
    url = f'https://www.sbpsranchi.in/Stn/stnImg1920/S-{num}.jpg'
    response = requests.get(url)

    if response.status_code == 200:
        # image found, send it to the user
        with open(f"{num}.jpg", 'wb') as f:
            f.write(response.content)
        bot.send_photo(chat_id=message.chat.id, photo=open(f"{num}.jpg", 'rb'))
        os.remove(f"{num}.jpg")  # delete the image file
    else:
        # image not found, send error message to the user
        bot.reply_to(message, f"IMAGE IS NOT AVAILABLE DUE TO OLD RECORD FOR {num}")

bot.polling()
