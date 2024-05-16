import RPi.GPIO as GPIO
from time import sleep
from lib import lcd
import board
from lib import clock
from lib import dht
from lib import dbContext

lcd = lcd()

clock = clock(lcd)
clock_thd = clock.run_async()

led = 22
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

dht = dht(board.D26)
dht_thread = dht.run_async()

db = dbContext()

print("DB file path: {f}".format(f = db.fullFilePath))

result = db.executeQuery("select sqlite_version();")
print('SQLite Version is {}'.format(result))

print(db.tableExists("settings"))


while True:
  if dht.isRunning:
    dht_data = dht.data
    if dht_data.temperature != None:
      lcd.display_string("Temp: {t} C".format(t = dht_data.temperature), 3)
    if dht_data.humidity != None:
      lcd.display_string(" Hum: {h} %".format(h = dht_data.humidity), 4)

  sleep(2)