import telebot
bot = telebot.TeleBot("1505627128:AAFZFQl8KfeBAKWzR8O9jfEVGTQ6MbuZ-40")

# считываем текст из файла и передаем в переменную v
with open('finalTeckers.txt') as tickers:
  listTickers = tickers.read()

@bot.message_handler(commands=['start'])
def send_welcome(message):
   bot.reply_to(message, "Привет, трейдер (или уже инвестор?) \nГотов выкупать просадки?")

@bot.message_handler(content_types=['text', 'document', 'audio'])
def echo_all(message):
   if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, трейдер (или уже инвестор?) \nГотов выкупать просадки? Следующие тикеры тебе подойдут: \n" + listTickers)
elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
   else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True)
