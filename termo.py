from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def thermometer():

    W = white
    R = red
    O= nothing

    logo = [
    O, O, W, W, W, W, O, O,
    O, O, W, O, O, W, O, O,
    O, O, W, O, O, W, O, O,
    O, O, W, O, O, W, O, O,
    O, O, W, O, O, W, O, O,
    O, O, W, O, O, W, O, O,
    O, O, W, O, O, W, O, O,
    O, W, W, W, W, W, W, O,
    ]
    return logo

s.set_pixels(thermometer())
count = 0
col_color =  (0, 255, 0)

while True:
  s.set_pixels(thermometer())
  temp = s.temp
  modulo= temp/19
  if temp < 19:
      s.set_pixel(3,(6),blue)
      s.set_pixel(4,(6),blue)
     
  elif temp > 20 and temp < 56:
      s.set_pixel(3,(6),yellow)
      s.set_pixel(4,(6),yellow)
     
  for x in range (0, int(modulo)):
    if temp > 20 and temp < 59:
        s.set_pixel(3,int(6-x),yellow)
        s.set_pixel(4,int(6-x),yellow)
    if temp > 60 and temp < 120:
        s.set_pixel(3,int(6-x),red)
        s.set_pixel(4,int(6-x),red)


