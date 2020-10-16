import Adafruit_DHT as dht22
import time
from providers.support.models import Metric

class TemperatureSensor:
    def __init__(self, data_pin):
        self.sensor = dht22.read_retry(dht22.DHT22, pin=data_pin)

    def read(self, retries=5):
        data_pin = 24
        temp_max = 20
        temp_min = 20

        result = dht22.read_retry(dht22.DHT22, pin=data_pin)
        humidity,temperature = result

        if len(result) == 0 and retries > 0:
            retries -= 1
            time.sleep(2)
            try:
                return self.read(retries)
            except:
                return []
        if len(result) > 0:
            return [
                Metric("pihome_temperature", round(temperature, 1)),
                Metric("pihome_humidity", round(humidity, 1))
            ]

        return []
