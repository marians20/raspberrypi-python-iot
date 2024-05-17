from dependency_injector import containers, providers
from lib import dht, lcd, clock
from api import api
import board

class Container(containers.DeclarativeContainer):
    """
    Check following url for documetation
    https://python-dependency-injector.ets-labs.org/
    """
    config = providers.Configuration()
    lcd = providers.Singleton(lcd)
    clock = providers.Singleton(clock, lcd)
    dht = providers.Singleton(dht, dht_pin=board.D26)
    api = providers.Singleton(api, dht)