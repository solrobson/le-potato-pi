import gpiod
from LePotatoPi.GPIO import consts
from LePotatoPi.GPIO import PulseWidthManagement as Pulse
from datetime import timedelta
from threading import Thread
import json
import time

class GPIO:
  used_pins = {}
  
  IN = 1
  OUT = 0

  BOARD = 10
  BCM = 11
  
  HIGH = 1
  LOW = 0

  PUD_OFF = 0
  PUD_DOWN = 1
  PUD_UP = 2

  NO_EDGE = 0
  RISING = 1
  FALLING = 2
  BOTH = 3


  def __init__(self):
    self.mode = self.BOARD
    self.chips = {
      "gpiochip0": gpiod.chip(consts.CHIP0),
      "gpiochip1": gpiod.chip(consts.CHIP1)
    }

  def setmode(self, mode):
    self.mode = mode
    
  
  def setup(self, pin, direction, pull_up_down=PUD_OFF, initial=None):
    mapped_pin = consts.LE_POTATO_PIN_TO_RPI_PIN[pin]

    print('checking for pin')
    if pin in self.used_pins:
      print('getting pin')
      p = self.used_pins[pin]
      print('releasing pin')
      p.release()
      print('pin released')
      print('deleting pin')
      del self.used_pins[pin]
      print('pin deleted')
      

    chip = self.chips[mapped_pin.chip]
    p = chip.get_line(mapped_pin.pin)
    bais = gpiod.line_request.FLAG_BIAS_DISABLE

    if pull_up_down == self.PUD_DOWN:
      bais = gpiod.line_request.FLAG_BIAS_PULL_DOWN
    elif pull_up_down == self.PUD_UP:
      bais = gpiod.line_request.FLAG_BIAS_PULL_UP
    else:
      bias = gpiod.line_request.FLAG_BIAS_DISABLE
    
    config = gpiod.line_request()
    config.consumer = "Blink"
    config.request_type = gpiod.line_request.DIRECTION_OUTPUT if direction == self.OUT else gpiod.line_request.DIRECTION_INPUT
    config.flags = bais

    p.request(config)
    self.used_pins[pin] = p

  def output(self, pin, level):
    p = self.used_pins[pin]
    p.set_value(level)
    print("output set")
    

  def input(self, channel):
    p = self.used_pins[channel]
    return p.get_value()

  def cleanup(self):
    while len(self.used_pins ) > 1:
      pinItem = self.used_pins.popitem()[1]
      print(dir(pinItem))
      pinItem.release()

  def PWM(self, pin, frequency):
    p = self.used_pins[pin]
    print("Pulse", dir(Pulse))
    return Pulse.PulseWidthManagement(p, frequency)
  
  def add_event_detect(self, gpio, edge, callback=None, bouncetime=None):
    pin_edge = self.NO_EDGE

    if edge == self.FALLING:
      pin_edge = gpiod.line_request.EVENT_FALLING_EDGE
    elif edge == self.RISING:
      pin_edge = gpiod.line_request.EVENT_RISING_EDGE
    else:
      pin_edge = gpiod.line_request.EVENT_BOTH_EDGES
    
    p = self.used_pins[gpio]

    config = gpiod.line_request()
    config.consumer = "Blink"
    config.request_type = pin_edge
    config.flags = p.bias
    dir(print(p))
    event_checker = Thread(target=self._read_event, args=(p, callback, bouncetime))
    event_checker.start()

  def _read_event(self, pin, callback, bouncetime):
    print(dir(self))
    if bouncetime == None:
      bouncetime = 10
    print(pin.direction)
    previous = pin.get_value()
    while pin.is_requested():
      #if pin.event_wait(timedelta(seconds=bouncetime)):
      if previous == pin.get_value():
        #print(previous, '==', pin.get_value())
        continue
      previous = pin.get_value()
      # There seem's to be a bug that is preventing the event_read() command from running.
      #  When this commands run an error return saying "No Such Device"  This error also occurs
      # in gpiomon
      # event = pin.event_read()
      # if event.event_type == pin.bias or event.event_type == gpiod.line_request.EVENT_BOTH_EDGES:
      callback()

