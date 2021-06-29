import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 64, auto_wire=False)
pixels.fill((255,0,0))
pixels.show()
