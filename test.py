import telebot




TOKEN = '1108625554:AAHcRaogrCxnYXF7U7MBt9UC-zb_PZR9zck'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def sms(message):
	if message.text == 'привет':
		bot.send_message(message.chat.id, 'привет')

bot.polling()