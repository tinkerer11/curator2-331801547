import telebot

bot = telebot.TeleBot('7796052816:AAHAS6Yq49CG3OTEjwKj_un36_aETrIg524')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Здравствуйте!')


@bot.message_handler(commands=['new'])
def new(message):
    bot.send_message(message.chat.id, 'Привет')


@bot.message_handler(commands=['video'])
def video(message):
    bot.send_message(message.chat.id, 'https://youtube.com/')


@bot.message_handler(commands=['help'])
def support(message):
    bot.send_message(message.chat.id, 'Нужна помощь!')


@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, 'Снова приветсвую!')


bot.infinity_polling()