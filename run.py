from time import sleep
import sys
import threading
from dependency_injector.wiring import Provide, inject
from container import Container
from flask import Flask, jsonify, Response
from lib import clock, lcd, dht
from api import api

@inject
def main(
   lcd : lcd = Provide[Container.lcd],
   dht : dht = Provide[Container.dht],
   clock : clock = Provide[Container.clock],
   api: api = Provide[Container.api],
) -> None:
  clock.run_async()
  dht.run_async()
  api.run_async()

  while True:
    if not dht.isRunning:
      continue
    dht_data = dht.data
    if dht_data.temperature != None:
      lcd.display_string("Temp: {t} C".format(t = dht_data.temperature), 3)
      print("Temp: {t} C".format(t = dht_data.temperature))
    if dht_data.humidity != None:
      lcd.display_string(" Hum: {h} %".format(h = dht_data.humidity), 4)
      print(" Hum: {h} %".format(h = dht_data.humidity))
    sleep(2)

if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[__name__])
    main(*sys.argv[1:])