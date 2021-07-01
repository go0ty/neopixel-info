import board
import neopixel
import time
import sys
from .stock import Stock

pixels = neopixel.NeoPixel(board.D18, 64, auto_write=False, brightness=0.2)
pixels.fill((0, 0, 0))
pixels.show()

stock = Stock()

def getColumnIndices(column):
    indices = []
    for x in range(0, 8):
        indices.append(column + (8 * x))
    return indices

def setPixelsForStock(percentChange, column):
    indices = getColumnIndices(column)
    if percentChange is None:
        for pixel in indices:
            pixels[pixel] = (0, 0, 0)
    else:
        if percentChange >= 0:
            pixels[indices[4]] = (0, 255, 0)
            if percentChange >= 2:
                pixels[indices[3]] = (0, 255, 0)
            if percentChange >= 4:
                pixels[indices[2]] = (0, 255, 0)
            if percentChange >= 6:
                pixels[indices[1]] = (0, 255, 0)
            if percentChange >= 8:
                pixels[indices[0]] = (0, 255, 0)
        else:
            pixels[indices[4]] = (255, 0, 0)
            if percentChange <= -2:
                 pixels[indices[5]] = (255, 0, 0)
            if percentChange <= -4:
                 pixels[indices[6]] = (255, 0, 0)
            if percentChange <= -6:
                 pixels[indices[7]] = (255, 0, 0)

while True:
    for index, (ticker, percentChange) in enumerate(stock.getCurrentPrices().items()):
        if ticker == 'SPY':
            pass
        else:
            setPixelsForStock(percentChange, index)
    pixels.show()
    time.sleep(20)
