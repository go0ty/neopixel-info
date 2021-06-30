from dotenv import load_dotenv
import os
import requests
import sched, time
import threading
import sys

load_dotenv()

API_KEY = os.getenv('STOCK_KEY')

class Stock:
    def __init__(self):
        self.prices = { 'SPY': None }
        for ticker in os.getenv('STOCK_TICKERS').split(','):
            self.prices[ticker] = None
        self.pollingQueue = list(self.prices.keys())
        self.schedule = sched.scheduler(time.time, time.sleep)
        pollingThread = threading.Thread(target=self.runPollingThread)
        pollingThread.start()

    def getCurrentPrices(self):
        return self.prices

    def runPollingThread(self):
        self.schedule.enter(1, 1, self.fetchNextPrice)
        self.schedule.run()

    def fetchNextPrice(self):
        ticker = self.pollingQueue[0]
        self.pollingQueue.remove(ticker)
        self.fetchPrice(ticker)
        self.pollingQueue.append(ticker)
        self.schedule.enter(15, 1, self.fetchNextPrice)

    def fetchPrice(self, ticker):
        price = None
        response = requests.get('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey={}&datatype=json'.format(ticker, API_KEY))
        if response.status_code == requests.codes.ok:
            data = response.json()
            if 'Note' not in data:
                if 'Global Quote' in data:
                    if '10. change percent' in data['Global Quote']:
                        price = data['Global Quote']['10. change percent']
        if price is None:
            print('Error polling price for {}, {} : {}'.format(ticker, response.status_code, data))
        else:
            self.prices[ticker] = price



stock = Stock()
print(stock.getCurrentPrices())