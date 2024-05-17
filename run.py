from time import sleep
import sys
from dependency_injector.wiring import Provide, inject

from container import Container

@inject
def main(
   lcd = Provide[Container.lcd],
   dht = Provide[Container.dht],
   clock = Provide[Container.clock],
) -> None:
  clock.run_async()
  dht.run_async()

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