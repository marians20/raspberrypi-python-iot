import adafruit_dht
import threading
from time import sleep
import json

class dhtData:
    def __init__(self, temperature, humidity):
        self.__temperature = temperature
        self.__humidity = humidity

    def toJSON(self):
        return json.dumps({
            "temperature": self.temperature,
            "humidity": self.humidity,
        })

    @property
    def temperature(self):
        return self.__temperature

    @property
    def humidity(self):
        return self.__humidity

class dht:
    def __init__(self, dht_pin):
        self.__dht_pin = dht_pin
        self.__temperature = None
        self.__humidity = None
        self.__can_continue = True
        self.__thd = None
        self.dhtDevice = adafruit_dht.DHT22(self.__dht_pin)

    def run_async(self):
        self.__thd = threading.Thread(target=self.__run, args=())
        self.__thd.start()
        return self.__thd

    @property
    def data(self):
        return dhtData(self.__temperature, self.__humidity)

    @property
    def isRunning(self):
        return self.__thd.is_alive and self.__can_continue

    @property
    def thread(self):
        return self.__thd

    def __run(self):
        while self.__can_continue:
            sleep(2)
            try:
                self.__temperature = self.dhtDevice.temperature
                self.__humidity = self.dhtDevice.humidity
            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print("Dht runtime error: {e}".format(e = error.args[0]))
                continue
            except Exception as error:
                # self.__can_continue = False
                print("Restarting DHT")
                self.dhtDevice.exit()
                self.dhtDevice = adafruit_dht.DHT22(self.__dht_pin)
                # raise error