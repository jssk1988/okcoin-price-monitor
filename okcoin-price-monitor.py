# -*- coding: utf-8 -*- 
# Date: 2014/1/23 15:29
# Author: sk
# Purpose: for chao bi, to make beep to alert warning!

import winsound
import time
import urllib2
import json
from sys import argv
import sys

#making sound of beep
def play_beep(interval):
	Freq = 2500 # Set Frequency To 2500 Hertz
	Dur = 1000 # Set Duration To 1000 ms == 1 second
	winsound.Beep(Freq,Dur)
	time.sleep(interval)

#Get web data in form of json
def get_data(web_site_api, currency_name):
	webdata = urllib2.urlopen(web_site_api).read()
	#json -> dict
	decodejson = json.loads(webdata)
	#the new currency price
	last_price = decodejson['return']['markets']['LTC']['lasttradeprice']
	print "The %s New Price: %s" % (currency_name, last_price)
	return last_price

def get_data2(web_site_api, currency_name):
	webdata = urllib2.urlopen(web_site_api).read()
	#json -> dict
	decodejson = json.loads(webdata)
	#the new currency price
	last_price = decodejson['ticker']['last']
	print "The %s New Price In Okcoin: %s" % (currency_name, last_price)
	return last_price
	
#main
if __name__ == "__main__":
	script, low_price, high_price = argv
	while 0 < 1:
		sys.stdout.flush()# flush the windows
		the_web_site = "http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=3"	
		the_web_site2 = "https://www.okcoin.com/api/ticker.do?symbol=btc_cny"
		the_web_site3 = "https://www.okcoin.com/api/ticker.do?symbol=ltc_cny"
		#print clock
		print time.strftime('%Y-%m-%d %A %X %Z',time.localtime(time.time()))
		try:
			ltc_price = get_data(the_web_site,"LTC") # ltc/btc
			btc_price = get_data2(the_web_site2, "BTC")  #btc/cny
			ltc_real_price = get_data2(the_web_site3, "LTC") #ltc/cny-real
		except:
			print "son of batch!web is over!"
			time.sleep(30*1) #should sleep, or print too fast
			continue
		#get_data(the_web_site+"btc_cny","BTC")
		#change unicode to float
		ltc_price_f = float(ltc_price) * float(btc_price)
		low_price = float(low_price)
		high_price = float(high_price)
		# compare with okcoin price
		ltc_price_ok = float(ltc_real_price)
		
		print "The LTC Real Price In Overseas: %f" % ltc_price_f #ltc/cny-real
		# break or not
		if ltc_price_ok >= high_price or ltc_price_ok <= low_price:
			print "Beep...\nCTRL-C to turn off."
			break
		#then sleep for 1 min
		time.sleep(60*1)
	while 0 < 1:
		the_real_interval = 1
		play_beep(the_real_interval)


