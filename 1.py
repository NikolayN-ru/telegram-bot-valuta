import telebot
import requests
import lxml.html
from lxml import etree
  
# @echobotmybot - телега

TOKEN = "5573906440:AAFQG6KPtk3y4JZlGVj4fVV-DST-v8PdTdE"
 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler()
def get_surname(message):
	html = requests.get('https://www.nbrb.by/statistics/rates/ratesdaily.asp').content 
	tree = lxml.html.document_fromstring(html)
	item=1
	while item<20:
		text = tree.xpath(f'//*[@id="ratesData"]/table/tbody/tr[{item}]/td[1]/div/span/text()')
		strMain = '//*[@id="ratesData"]/table/tbody/tr[%s]/td[3]/div/text()' %(item)
		countValue = '//*[@id="ratesData"]/table/tbody/tr[%s]/td[2]/text()' %(item)
		if message.text == text[0]:
			value = tree.xpath(strMain)
			countValue2 = tree.xpath(countValue)
			bot.reply_to(message, f'{countValue2[0]} к белорусскому рублю == {value[0]}')
			return
		else:
			pass
		item += 1
	bot.reply_to(message, 'валюта неизвестна')

bot.polling(none_stop=True)