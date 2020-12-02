import telebot
import urllib
import re,os,sys

from urllib import request
from urllib.parse import quote
from telebot import types

key= os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(key)
alphabet = ['Ь', 'ь', 'Ъ', 'ъ', 'А', 'а', 'Б', 'б', 'В', 'в', 'Г', 'г', 'Д', 'д', 'Е', 'е', 'Ё', 'ё',
            'Ж', 'ж', 'З', 'з', 'И', 'и', 'Й', 'й', 'К', 'к', 'Л', 'л', 'М', 'м', 'Н', 'н', 'О', 'о',
            'П', 'п', 'Р', 'р', 'С', 'с', 'Т', 'т', 'У', 'у', 'Ф', 'ф', 'Х', 'х', 'Ц', 'ц', 'Ч', 'ч',
            'Ш', 'ш', 'Щ', 'щ', 'Ы', 'ы', 'Э', 'э', 'Ю', 'ю', 'Я', 'я']
@bot.message_handler(commands=['start'])
def welcome(message):
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы находить вам нужые видео. Пишите аглийскими симбволами.".format(message.from_user, bot.get_me()),
        parse_mode='html')
 
@bot.message_handler(content_types=['text'])
def lalala(message):
            mas=''
            umr=''
            for x in message.text:
                if x==' ':
                    umr+='+'
                else:
                    umr+=x
            if list(set(alphabet) & set(message.text)):
                bot.send_message(message.chat.id,"сообщения должны быть на англиском")
            else:
                sq='https://www.youtube.com/results?search_query='+umr
                doc=urllib.request.urlopen(sq).read().decode('cp1251',errors='ignore')
                match=re.findall("\?v\=(.+?)\"",doc)
                if match:
                    for ii in match:
                        if (len(ii)<25):
                            mas="https://www.youtube.com/watch?v="+ii
                            break
                bot.send_message(message.chat.id, mas)
                mas=dict(zip(mas,mas)).values()
# RUN
bot.polling(none_stop=True)
