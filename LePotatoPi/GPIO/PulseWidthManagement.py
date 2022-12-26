#from LePotatoPi.GPIO.GPIO import GPIO

from threading import Thread
import time
class PulseWidthManagement(Thread):
	def __init__(self, pin, frequency):
		self.pin = pin
		self.frequency = frequency
		self.max_cycle = 100.0
		self.duty_cycle = 0
		self.pulse_time = 1.0/frequency
		self.slice = self.pulse_time / self.max_cycle
		self.to_stop = False
		self.stopped = False


	def start(self, duty_cycle):
		self.duty_cycle = duty_cycle
		self.thread = Thread(None, self._pulse_loop)
		self.thread.start()

	def stop(self):
		while self.stopped == false:
			self.to_stop = True
			time.sleep(0.01)

	def ChangeDutyCycle(self, duty_cycle):
		self.duty_cycle = duty_cycle

	def _pulse_loop(self):
		while self.to_stop == False:
			self.pin.set_value(1)
			time.sleep(self.duty_cycle * self.slice)
			self.pin.set_value(0)
		self.stopped = True

