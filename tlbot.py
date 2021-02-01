import telebot
import datetime
bot = telebot.TeleBot('1584941829:AAH8YRZt6r4lwJXAFNmT03rktShCntGB25s')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет','Пока')
keyboard1.row('Дата','Время','День недели')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Добро пожаловать в UlanaMeta бот!!!',reply_markup=keyboard1)
@bot.message_handler(content_types=['text'])
def send_text(message):
    a = datetime.date.today()
    b = datetime.datetime.today()
    if message.text.title() == 'Привет':
        bot.send_message(message.chat.id,'И тебе привет!',reply_markup=keyboard1)
    elif message.text.title() == 'Пока':
        bot.send_message(message.chat.id,'Покакаешь дома :)',reply_markup=keyboard1)
    elif message.text.title() == 'Дата':
        bot.send_message(message.chat.id,str(a),reply_markup=keyboard1)
    elif message.text.title() == 'Время':
        bot.send_message(message.chat.id,b,reply_markup=keyboard1)
    elif message.text.title() == 'День недели':
        d = datetime.datetime.today()
        r = d.weekday
        if r == 0:
            c = 'понедельник'
        elif r == 1:
            c = 'вторник'
        elif r == 2:
            c = 'среда'
        elif r == 3:
            c = 'четверг'
        elif r == 4:
            c = 'пятница'
        elif r == 5:
            c = 'суббота'
        elif r == 6:
            c = 'воскресенье'
        bot.send_message(message.chat.id,str(c),reply_markup=keyboard1)
bot.polling()