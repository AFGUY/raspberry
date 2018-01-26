
###########################################################################
#Filename      :BMP180test1.py
#Description   :Using Bmp180 sensor and a Telegram Bot
#Author        :Riccardo Pestrin
#Website       :pestrinriccardo.altervista.org
#Update        :2018/01/25
############################################################################
 
import time
import sys
import os
import telepot
from telepot.loop import MessageLoop
import datetime
from datetime import datetime

from BMP180 import BMP180

bmp = BMP180()

id_a = [47313852]


def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	sender = msg['from']['id']
	print 'Got command: %s' % command
	if sender in id_a:
		if command == '/start':
			if sender == 47313852:
				bot.sendMessage(chat_id, 'Ciao Riccardo!')
			else:
				bot.sendMessage(chat_id, 'Hei, ciao!')
			print chat_id
		elif command == '/meteo':
			pressure = bmp.read_pressure()
			if(pressure >= 101500):
				bot.sendMessage(chat_id, 'Prevedo bel tempo.')
			elif(pressure <= 100700):
				bot.sendMessage(chat_id, 'Prevedo brutto tempo.')
			else:
				bot.sendMessage(chat_id, 'Prevedo tempo instabile.')
		elif command == '/temperatura':
			temp = bmp.read_temperature()
			bot.sendMessage(chat_id, 'La temperatura in salotto e\' di '+str(temp)+' gradi centigradi.')
		elif command == '/ora':
				bot.sendMessage(chat_id, 'Sono le '+time.strftime("%H:%M:%S"))
		elif command == '/data':
			i = datetime.now()
			if(time.strftime("%a") == 'Mon'):
				giorno = 'Lunedi\''
			if(time.strftime("%a") == 'Tue'):
				giorno = 'Martedi\''
			if(time.strftime("%a") == 'Thu'):
				giorno = 'Mercoledi\''
			if(time.strftime("%a") == 'Wed'):
				giorno = 'Giovedi\''
			if(time.strftime("%a") == 'Fri'):
				giorno = 'Venerdi\''
			if(time.strftime("%a") == 'Sat'):
				giorno = 'Sabato\''
			if(time.strftime("%a") == 'Sun'):
				giorno = 'Domenica\''
			bot.sendMessage(chat_id, 'Oggi e\' '+giorno+' '+'%s/%s/%s'% (i.day, i.month, i.year))
		else:
			bot.sendMessage(chat_id, 'Non capisco il comando.')	
	else:
		bot.sendMessage(chat_id, 'Non sei autorizzate a darmi ordini! Il tuo chat ID non e\' nella lista.')
		bot.sendMessage(chat_id, sender)
		print chat_id
bot = telepot.Bot('459932785:AAGjA3UjxB3TIdkhDPgT--sj11vTQa6EzME')
bot.message_loop(handle)

print 'Sono in ascolto...'
 
while 1:
    time.sleep(10)









 

