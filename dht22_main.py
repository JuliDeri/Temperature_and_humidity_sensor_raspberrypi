```python
# Import necessary libraries
import board
import adafruit_dht
import time

# Initialize the DHT device
dht_device = adafruit_dht.DHT22(board.D4)

# Loop to continuously read data from the sensor
while True:
    try:
        # Read temperature and humidity from the sensor
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity

        # Get the current time
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        # Print the values to the console
        print(f"Time: {current_time} - Temperature: {temperature_c}C, Humidity: {humidity}%")

    except RuntimeError as error:
        # Handle errors related to reading the sensor
        print(f"Error reading sensor: {error.args[0]}")

    # Wait for 20 seconds before taking another reading
    time.sleep(20.0)
```
