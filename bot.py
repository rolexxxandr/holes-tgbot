import telebot
import config
from functions import count_holes

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def welcome(message):
    bot.send_message(message.chat.id, "/q")

@bot.message_handler(commands=["github"])
def git_hub(message):
    bot.send_message(message.chat.id, "https://github.com/rolexxxandr")

@bot.message_handler(content_types=["text"])
def send_result(message):
    bot.send_message(message.chat.id, f"Holes: {count_holes(message.text)}")

# RUN
bot.polling(none_stop=True)