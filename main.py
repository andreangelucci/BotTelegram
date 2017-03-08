import telegram
import configparser
import redis
import sys
import loteriaFederal.loteriaFederal
import quina.webCrawlerQuina

from telegram.ext import Updater
from telegram.ext import Updater, CommandHandler

reload(sys)
sys.setdefaultencoding('utf-8')

# Configura o bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

# Connecting to Telegram API
# Updater retrieves information and dispatcher connects commands
updater = Updater(token=config['DEFAULT']['token'])
dispatcher = updater.dispatcher

# Connecting to Redis db
db = redis.StrictRedis(host=config['DB']['host'],
                       port=config['DB']['port'],
                       db=config['DB']['db'])

def start(bot, update):
    """
        Mensagem de boas vindas.
    """
    me = bot.get_me()

    # Welcome message
    msg = "Fala marreco!\n"
    msg += "Qual a bronca?\n"
    msg += "Seu id eh {0}.\n".format(update.message.chat_id)    

    # Commands menu
    main_menu_keyboard = [[telegram.KeyboardButton('/loteriaFederal')],
                          [telegram.KeyboardButton('/quina')]]
    reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
                                                   resize_keyboard=True,
                                                   one_time_keyboard=True)

    # Send the message with menu
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg,
                     reply_markup=reply_kb_markup)

def resultadoLoteriaFederal(bot, update):    
    msg = loteriaFederal.loteriaFederal.crawler()
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)

def resultadoQuina(bot, update):
    msg = quina.webCrawlerQuina.crawler()
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg)

#associa os comandos
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

loteriaFederal_handler = CommandHandler('loteriaFederal', resultadoLoteriaFederal)
dispatcher.add_handler(loteriaFederal_handler)

quina_handler = CommandHandler('quina', resultadoQuina)
dispatcher.add_handler(quina_handler)