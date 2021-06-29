import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 64, auto_write=False, brightness=0.5)
pixels.fill((0,0,0))
pixels.show()
