import time
import random
import datetime
import json
import telepot
import requests
from telepot.loop import MessageLoop

amount = 0
start=0
miningAddress = ''		""" Insert Mining Address """
chatId = 			""" Insert chatID """
telegramBot = ''		""" Insert Telegram Bot Key """
while True:
    try:
        if start == 0:
            bot = telepot.Bot(telegramBot) 
            bot.sendMessage(chatId, "Initiated Script" ) 
            r = requests.get('http://walchain.info:18950/api/getBalance/'+miningAddress)
            data = r.text
            j= json.loads(data)
            r2 = requests.get('http://walchain.info:18950/api/getMinedBlocksPagination/'+miningAddress+'/1/5000')
            r2 = requests.get('http://beelazy.de/test.php')
            data2 = r2.text
            j2= json.loads(data2)
            amount = str(j2['return_counts'])
            print(str(j2['return_counts']))
            start=1
            time.sleep(10)
        else:
            bot = telepot.Bot(telegramBot) 
            r = requests.get('http://walchain.info:18950/api/getBalance/'+miningAddress) 
            data = r.text
            j= json.loads(data)
            r2 = requests.get('http://walchain.info:18950/api/getMinedBlocksPagination/'+miningAddress+'/1/5000')
            data2 = r2.text
            j2= json.loads(data2)
            amount2 = j2['return_counts']
            if (int(amount2)>int(amount)):
                amount = j2['return_counts']
                bot.sendMessage(chatId, "Mined a new Block!!!\r\n"+"New Balance:" + str(j['Balance']) + " WTC\r\nBlocks mined:" +str(amount) )
                time.sleep(10)
            else:
                time.sleep(10)
    except KeyError, e:
        time.sleep(5)
