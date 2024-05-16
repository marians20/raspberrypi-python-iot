# A simple program to test the driver

from time import sleep
from htu21df import htu21df

htu21 = htu21df()

while True:
	print("sending reset...")
	htu21.htu_reset
	temperature = htu21df.read_temperature()
	print("The temperature is %f C." % temperature)
	humidity = htu21.read_humidity()
	print("The humidity is %F percent." % humidity)
	sleep(1)
