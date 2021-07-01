import board
import neopixel
import time
import sys
from .stock import Stock

pixels = neopixel.NeoPixel(board.D18, 64, auto_write=False, brightness=0.2)

stock = Stock()

def getPixelsForStock(percentChange, column):
    pass

while True:
    for index, (ticker, percentChange) in stock.getCurrentPrices():
        if ticker == 'SPY':
            pass
        else:
            getPixelsForStock(percentChange, index)

    time.sleep(20)