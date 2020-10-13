import sys
import Adafruit_DHT as adht

pin = 24
humidity,temperature = adht.read_retry(adht.DHT22, pin)
if humidity is not None and temperature is not None:
    print( 'humidity:', round(humidity,1) , 'temperature:', round(temperature,1))
    print( 'humidity: {0:0.1f} and temperature: {1:0.1f} C'.format(humidity, temperature))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
