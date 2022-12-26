from LePotatoPi.GPIO.BoardPinSettings import BoardPinSettings


CHIP0 = "gpiochip0"
CHIP1 = "gpiochip1"

#Mapping of the le Potato pins to Raspberry Pi
LE_POTATO_PIN_TO_RPI_PIN = {
  2: BoardPinSettings(CHIP0, 5),
  3: BoardPinSettings(CHIP0, 4),
  4: BoardPinSettings(CHIP1, 98),
  17: BoardPinSettings(CHIP0, 8),
  27: BoardPinSettings(CHIP0, 9),
  22: BoardPinSettings(CHIP0, 10),
  10: BoardPinSettings(CHIP1, 87 ),
  9: BoardPinSettings(CHIP1, 88),
  11: BoardPinSettings(CHIP1, 90),
  0: BoardPinSettings(CHIP1, 75),
  5: BoardPinSettings(CHIP1, 96),
  6: BoardPinSettings(CHIP1, 97),
  13: BoardPinSettings(CHIP1, 85),
  19: BoardPinSettings(CHIP1, 86),
  26: BoardPinSettings(CHIP1, 84),
  14: BoardPinSettings(CHIP1, 91),
  15: BoardPinSettings(CHIP1, 92),
  18: BoardPinSettings(CHIP0, 6),
  23: BoardPinSettings(CHIP1, 93),
  24: BoardPinSettings(CHIP1, 94),
  25: BoardPinSettings(CHIP1, 79),
  8: BoardPinSettings(CHIP1, 89),
  7: BoardPinSettings(CHIP1, 80),
  1: BoardPinSettings(CHIP1, 76),
  12: BoardPinSettings(CHIP1, 95),
  16: BoardPinSettings(CHIP1, 81),
  20: BoardPinSettings(CHIP1, 82),
  21: BoardPinSettings(CHIP1, 83)
}

LE_POTATO_BOARD_MAPPING = {
  3: BoardPinSettings(CHIP0, 5),
  5: BoardPinSettings(CHIP0, 4),
  7: BoardPinSettings(CHIP1, 98),
  11: BoardPinSettings(CHIP0, 8),
  13: BoardPinSettings(CHIP0, 9),
  15: BoardPinSettings(CHIP0, 10),
  19: BoardPinSettings(CHIP1, 87),
  21: BoardPinSettings(CHIP1, 88),
  23: BoardPinSettings(CHIP1, 90),
  27: BoardPinSettings(CHIP1, 75),
  29: BoardPinSettings(CHIP1, 96),
  31: BoardPinSettings(CHIP1, 97),
  33: BoardPinSettings(CHIP1, 85),
  35: BoardPinSettings(CHIP1, 86),
  37: BoardPinSettings(CHIP1, 84),
  8: BoardPinSettings(CHIP1, 91),
  10: BoardPinSettings(CHIP1, 92),
  12: BoardPinSettings(CHIP0, 6),
  16: BoardPinSettings(CHIP1, 93),
  18: BoardPinSettings(CHIP1, 94),
  22: BoardPinSettings(CHIP1, 79),
  24: BoardPinSettings(CHIP1, 89),
  26: BoardPinSettings(CHIP1, 80),
  28: BoardPinSettings(CHIP1, 76),
  32: BoardPinSettings(CHIP1, 95),
  36: BoardPinSettings(CHIP1, 81),
  38: BoardPinSettings(CHIP1, 82),
  40: BoardPinSettings(CHIP1, 83)
}
