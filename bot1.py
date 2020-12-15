import telebot
import html5lib
import re,os,sys
import urllib.request

from bs4 import BeautifulSoup
from telebot import types

bot = telebot.TeleBot('1411970649:AAGoRd2jMQIUQLMOxp7iZ2yg5fqFWOBm0ao')
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
            link=''
            for x in message.text:
                if x==' ':
                    umr+='+'
                else:
                    umr+=x
            if list(set(alphabet) & set(message.text)):
                bot.send_message(message.chat.id, "сообщения должны быть на анлийском")
            else:
                sq='https://www.youtube.com/results?search_query='+umr
                doc=urllib.request.urlopen(sq).read().decode('utf-8','ignore')
                match=re.findall("\?v\=(.+?)\"",doc)
                if match:
                    for ii in match:
                        if (len(ii)<25):
                            mas="https://www.youtube.com/watch?v="+ii
#                            link=getlink(ii)
                            break
#                markup = types.InlineKeyboardMarkup(row_width=2)
 #               item1 = types.InlineKeyboardButton("Скачать", url=link)
 #               markup.add(item1)
 #reply_markup=markup
                bot.send_message(message.chat.id, mas)
                mas=dict(zip(mas,mas)).values()

#def getlink(ii):
#    mas="https://www.ssyoutube.com/watch?v="+ii
 #   sauce = urllib.request.urlopen(mas)
 #   soup = BeautifulSoup(sauce, 'lxml')
  #  body=soup.body
   # for url in body.find_all(attrs={"class": "link link-download subname ga_track_events download-icon"}):
    #    link = url.get('href')
     #   break
   # return link
# RUN
bot.polling(none_stop=True)