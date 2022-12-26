import gpiod
from LePotatoPi.GPIO import consts
from LePotatoPi.GPIO import PulseWidthManagement as Pulse

class GPIO:
  used_pins = {}
  IN = 1
  OUT = 0

  BOARD = 10
  BCM = 11
  
  HIGH = 1
  LOW = 0

  def __init__(self):
    self.mode = self.BOARD
    self.chips = {
      "gpiochip0": gpiod.chip(consts.CHIP0),
      "gpiochip1": gpiod.chip(consts.CHIP1)
    }

  def setmode(self, mode):
    self.mode = mode
    
  
  def setup(self, pin, mode, initial = None):
    #setup(pin, GPIO.OUT, initial = GPIO.HIGH)
    mapped_pin = consts.LE_POTATO_PIN_TO_RPI_PIN[pin]
    #print(mapped_pin.chip)
    chip = self.chips[mapped_pin.chip]
    #print("chip {}, pin {}", chip.name, pin)
    p = chip.get_line(mapped_pin.pin)
    #print(dir(p))
    config = gpiod.line_request()
    config.consumer = "Blink"
    config.request_type = gpiod.line_request.DIRECTION_OUTPUT if mode == self.OUT else gpiod.line_request.DIRECTION_INPUT
    config.flags = gpiod.line_request.FLAG_BIAS_PULL_UP

    p.request(config)
    self.used_pins[pin] = p

  def output(self, pin, level):
    #print("output: ", pin, level)
    #print(self.used_pins)
    p = self.used_pins[pin]
    #print(dir(p))
    p.set_value(level)
    print("output set")

  def cleanup(self):
    while len(self.used_pins ) > 1:
      pinItem = self.used_pins.popitem()
     # print("Releasing pin : ", self.used_pins)
      pinItem.release()

  def PWM(self, pin, frequency):
   # self.setup(pin, self.OUT)
    p = self.used_pins[pin]
    print("Pulse", dir(Pulse))
    return Pulse.PulseWidthManagement(p, frequency)
