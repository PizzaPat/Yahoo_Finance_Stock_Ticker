import main
import os
import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from os import system



def start_ticker():
	system('cls')
	print('%9s  %9s  %9s  %9s  %15s  %15s'%('Ticker','Price','Open','Close','Volume','Ave. Volume'))
	print('-----------------------------------------------------------------------------')
	with open('../data/ticker.txt','r') as f:
		# f_contents = f.readline()
		# print(f_contents, end='')
		# f_contents = f.readline()
		# print(f_contents, end='')
		for line in f:
			try:
				ticker = line.strip('\n')
				my_url = 'https://finance.yahoo.com/quote/'+ticker+'?p='+ticker
				uClient = uReq(my_url)
				page_html = uClient.read()
				page_soup = soup(page_html,'html.parser')
				curPrice = page_soup.findAll("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
				openPrice = page_soup.findAll("td",{"data-test":"OPEN-value"})
				closePrice = page_soup.findAll("td",{"data-test":"PREV_CLOSE-value"})
				volumn = page_soup.findAll("td",{"data-test":"TD_VOLUME-value"})
				aveVolumn = page_soup.findAll("td",{"data-test":"AVERAGE_VOLUME_3MONTH-value"})
				print('%9s  %9s  %9s  %9s  %15s  %15s'%(ticker,curPrice[0].text,openPrice[0].text,closePrice[0].text,volumn[0].text,aveVolumn[0].text))
				# print('Close price: ', closePrice[0].text)
			except:
				print(ticker, ': Invalid ticker')
		print()
		pass

def add_ticker(stock):
	with open('../data/ticker.txt','a') as f:
		request = requests.get('https://finance.yahoo.com/quote/'+stock+'?p='+stock)
		if request.status_code == 200:
			f.write('\n'+stock)
		else:
			print('Invalid ticker')


def remove_ticker(stock):
	with open('../data/ticker.txt', 'r') as rf:
		with open('../data/ticker_tmp.txt', 'w') as wf:
			for line in rf:
				curTicker = line.strip('\n')
				print('->',curTicker)
				if stock != curTicker:
					wf.write(curTicker+'\n')
	os.remove('../data/ticker.txt')
	os.rename('../data/ticker_tmp.txt', '../data/ticker.txt')

	# 	