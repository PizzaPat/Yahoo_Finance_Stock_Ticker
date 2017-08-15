from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import argparse
import ticker

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--start', help="Print the ticker(s) that is/are saved",choices=['ticker'])
	parser.add_argument('--add', help="Add a stock ticker")
	parser.add_argument('--remove', help="Remove a stock ticker")
	args = parser.parse_args()
	if args.add:
		ticker.add_ticker(args.add)
	
	if args.remove:
		ticker.remove_ticker(args.remove)
	
	if args.start == 'ticker':
		ticker.start_ticker()
