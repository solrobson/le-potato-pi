import gpiod
import consts


class GPIO:
  used_pins = {}
  INPUT = 1
  OUTPUT = 0

  BOARD = 10
  BCM = 11
  
  HIGH = 1
  LOW = 1

  def __init__(self):
    self.mode = self.BOARD
    self.chips = {
      0: gpiod.chil(consts.CHIP0),
      1: gpiod.chip(consts.CHIP1)
    }

  def setmode(self, mode):
    self.mode = mode
    
  
  def setup(self, pin, mode, initial = None):
    #setup(pin, GPIO.OUT, initial = GPIO.HIGH)
    mapped_pin = consts.LE_POTATO_PIN_TO_RPI_PIN[pin]
    p = mapped_pin.chip.get_line(pin)
    config = gpiod.line_request()
    config.consumer = "Blink"
    config.request_type = gpiod.line_request.DIRECTION_OUTPUT if mode == self.OUTPUT else gpiod.line_request.DIRECTION_INPUT
    config.flags = gpiod.line_request.FLAG_BIAS_PULL_UP

    p.request(config)
    self.used_pins[pin] = p

  def output(self, pin, level):
    p = self.used_pins[pin]
    p.set_value(level)

  def cleanup(self):
    pass

