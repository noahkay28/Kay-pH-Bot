from atlas_i2c import atlas_i2c
from Adafruit_IO import Client, Feed

io_key = "94921b4b90264ebbb2b0fc9a08137e9e"
io_username = "reginius214"

aio = Client(io_username, io_key)
pH_feed = aio.feeds('kay-ph')
sensor_address = 2
pH_sensor = atlas_i2c.AtlasI2C()
pH_sensor.set_i2c_address(sensor_address)

reading = pH_sensor.query("R", processing_delay=1500)

pH = reading.data

pH = round(float(pH.decode("utf-8")),1)

print(pH)

aio.send(pH_feed.key, str(pH))