import telebot
import config
import data_main
from com_create import com_create
from com_list import com_list
from com_join import com_join
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,
    "Добро пожаловать, {0.first_name}!\nЯ - "
    "<b>{1.first_name}</b>, бот созданный чтобы получить зачет по экономике.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id, config.COMMANDS_LINE)


@bot.message_handler(content_types=['text'])
def catch(message):
    if message.chat.type == 'private':
        text = message.text
        fw = text.split()[0]
        if len(text.split()) < 2:
            bot.send_message(message.chat.id, 'Не понимаю 😢')
            bot.send_message(message.chat.id, config.COMMANDS_LINE)
        com = ' '.join(text.split()[1:])
        if fw == '!create':
            if com_create(message, com, bot) is False:
                return

        elif message.text == '!list':
            if com_list(message, com, bot) is False:
                return

        elif message.text == '!join':
            if com_join(message, com, bot) is False:
                return
        else:
            bot.send_message(message.chat.id, 'Не понимаю 😢')
            bot.send_message(message.chat.id, config.COMMANDS_LINE)


bot.polling(none_stop=True)

