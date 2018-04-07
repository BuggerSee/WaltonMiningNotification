import time
import random
import datetime
import json
import urllib2
import telepot
import requests
from telepot.loop import MessageLoop

amount = 0
start=0
miningAddress = ''
chatId = ''
telegramBot = ''
while True:
    try:
        if start == 0:
            bot = telepot.Bot(telegramBot) 
            bot.sendMessage(chatId, "Initiated Script" ) 
            start=1
            r = requests.get('http://walchain.info:18950/api/getBalance/'+miningAddress)
            data = r.text
            j= json.loads(data)
            r2 = requests.get('http://walchain.info:18950/api/getMinedBlocksPagination/'+miningAddress+'/1/5000')
            data2 = r2.text
            j2= json.loads(data2)
            amount = str(j2['return_counts'])
            time.sleep(10)
        else:
            bot = telepot.Bot(telegramBot) 
            r = requests.get('http://walchain.info:18950/api/getBalance/'+miningAddress) 
            data = r.text
            j= json.loads(data)
            r2 = requests.get('http://walchain.info:18950/api/getMinedBlocksPagination/'+miningAddress+'/1/5000')
            data2 = r2.text
            j2= json.loads(data2)
            if j2['return_counts'] > amount:
                amount = j2['return_counts']
                bot.sendMessage(chatId, "Balance:" + str(j['Balance']) + " WTC\r\nBlocks mined:" +str(amount) )
                time.sleep(10)
            else:
                time.sleep(10)
    except KeyError, e:
        time.sleep(5)