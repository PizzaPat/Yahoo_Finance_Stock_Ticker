# Yahoo Finance Stock Ticker

![yh-ticker](https://github.com/PizzaPat/Yahoo_Finance_Stock_Ticker/blob/master/screenshots/startTicker.png)

[![PyPI](https://img.shields.io/pypi/v/Yahoo_Finance_Stock_Ticker.svg)](https://pypi.python.org/pypi/Yahoo_Finance_Stock_Ticker)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()

## About:
This is an open source web scraping python package. The package helps stock broker to take a quick look at the open, the previous close, the volume, and the average volume of any stock. This package does not include graphical analysis or press releases. This package includes bs4 for web scraping and argparse for options

## Requirements:
[Python 3.6](https://www.python.org/downloads/release/python-361/)

[pip](https://bootstrap.pypa.io/get-pip.py)

### pip installation:
- Go [https://bootstrap.pypa.io/get-pip.py](https://bootstrap.pypa.io/get-pip.py)
- Right click, "Save as...", choose the target location
- ```cd``` to that directory. type ```python get-pip.py```
- Done

## Installation:
```pip install yahoo_finance_stock_ticker```

## Usage:
- The package can be called by keyword ```yh-ticker```
- IMPORTANT: After the installation, you must create an empty list of stock by ```yh-ticker --create list```. This will create an empty text file to hold the record of stock you have added/removed

![createList](https://github.com/PizzaPat/Yahoo_Finance_Stock_Ticker/blob/master/screenshots/createList.png)

![afterCreateList](https://github.com/PizzaPat/Yahoo_Finance_Stock_Ticker/blob/master/screenshots/afterCreateList.png)

## Commands:
- ```yh-ticker --add <symbol>```. Adds the symbol of the stock to the text file, replace <symbol> with your desire stock symbol, e.g. ```yh-ticker --add GOOGL```
- ```yh-ticker --remove <symbol>```. Removes the symbol of the stock from the text file, replace <symbol> with your desire stock symbol, e.g. ```yh-ticker --remove GOOGL```
- ```yh-ticker --create list```. Creates new text file for tickers. Users must initiate this command before add/remove/start tickers. You can also complete remove all tickers by this command as well
- ```yh-ticker --start ticker```. Start scraping the current tickers' information and display it on the terminal from Yahoo Finance website.
- ```yh-ticker -h```. Get information about options
