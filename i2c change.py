from atlas_i2c import atlas_i2c

sensor_address = 99
pH_sensor = atlas_i2c.AtlasI2C()
pH_sensor.set_i2c_address(sensor_address)

reading = pH_sensor.query("i2c, 2")
