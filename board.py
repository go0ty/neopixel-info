import board
import neopixel
import time
import sys
from .stock import Stock

pixels = neopixel.NeoPixel(board.D18, 64, auto_write=False, brightness=0.2, pixel_order=neopixel.RGB)
pixels[0] = (255,0,0)
pixels[63] = (0,255,0)
pixels[7] = (0,0,255)
pixels.show()
sys.exit(1)

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