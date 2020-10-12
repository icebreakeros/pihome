import Adafruit_DHT as dht22
import time
from providers.support.models import Metric

class TemperatureSensor:
    def __init__(self, data_pin):
        self.sensor = dht22.read_retry(dht22.DHT22, pin=data_pin)

    def read(self, retries=5):
        result = self.sensor
        humidity,temperature = result

        if len(result) == 0 and retries > 0:
            retries -= 1
            time.sleep(1)
            try:
                return self.read(retries)
            except:
                return []
        if len(result) > 0:
            return [
                Metric("pihome_temperature", int(temperature)),
                Metric("pihome_humidity", int(humidity))
            ]

        return []
