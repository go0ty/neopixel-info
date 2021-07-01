import board
import neopixel
import time
import sys
from stock import Stock

pixels = neopixel.NeoPixel(board.D18, 64, auto_write=False, brightness=0.2)
pixels.fill((0, 0, 0))
pixels.show()

stock = Stock()

def getColumnIndices(column):
    indices = []
    for x in range(0, 8):
        indices.append(column + (8 * x))
    return indices

def getRowIndices(spyPercent):
    row = None
    if spyPercent >= 4:
        row = 0
    elif spyPercent >= 3:
        row = 1
    elif spyPercent >= 2:
        row = 2
    elif spyPercent >= 1:
        row = 3
    elif spyPercent >= 0:
        row = 4
    elif spyPercent >= -1:
        row = 5
    elif spyPercent >= -2:
        row = 6
    else:
        row = 7
    firstPixel = row * 8
    indices = [ firstPixel ]
    for x in range(1, 8):
        indices.append(firstPixel + x)
    return indices

def setSpyBar(percentChange):
    if percentChange is not None:
        rowIndices = getRowIndices(percentChange)
        for pixel in rowIndices:
            pixels[pixel] = (50, 50, 50)

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
            setSpyBar(percentChange)
        else:
            setPixelsForStock(percentChange, index)
    pixels.show()
    time.sleep(30)
