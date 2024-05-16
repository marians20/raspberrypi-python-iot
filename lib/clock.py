
import threading
from time import sleep
from datetime import datetime
import math
from lib import lcd

class clock:
    def __init__(self, lcd):
        self.lcd = lcd
        
    def run_async(self):
        thd = threading.Thread(target=self.__run, args=())
        thd.start()
        return thd

    def __run(self):
        previousMillisecond = -1
        while True:
            now = datetime.now()
            millisecond = math.floor(now.microsecond / 100000)
            if millisecond != previousMillisecond and millisecond % 5 == 0:
                previousMillisecond = millisecond
                if millisecond == 5:
                    dateTimeString = "{d} {t}".format(d = now.strftime('%d-%m-%Y'), t = now.strftime('%H:%M %S'))
                else:
                    dateTimeString = "{d} {t}".format(d = now.strftime('%d-%m-%Y'), t = now.strftime('%H:%M:%S'))
                self.lcd.display_string(dateTimeString, 1)
            sleep(0.1)
