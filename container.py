from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from lib import dht, lcd, clock
import board

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    lcd = providers.Singleton(lcd)
    clock = providers.Singleton(clock, lcd)
    dht = providers.Singleton(
        dht,
        dht_pin=board.D26
    )