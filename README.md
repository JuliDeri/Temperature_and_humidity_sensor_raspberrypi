# DHT22 Sensor Data Logger

## Project Overview

This project uses a DHT22 sensor connected to a Raspberry Pi to continuously read and log temperature and humidity data. The data is collected and printed to the console. The ultimate goal is to automate the process of sending this data to a laptop daily for visualization using Pyplot.

## Setup and Installation

### 1. SSH Connection to Raspberry Pi

Ensure you can connect to your Raspberry Pi via SSH. If needed, refer to the [SSH setup guide](https://www.raspberrypi.org/documentation/remote-access/ssh/) for more details.

### 2. Install Required Libraries

1. **Update Package List**:

    ```bash
    sudo apt-get update
    ```

2. **Install Required Python Libraries**:

    ```bash
    sudo apt-get install python3-pip
    sudo pip3 install adafruit-circuitpython-dht
    ```

3. **Install Additional Required Libraries** (if any):

    ```bash
    sudo apt-get install libgpiod2
    ```
### 3. Hardware setup and wiring
The left pin of the sensor connects to the 3.3V pin on the Raspberry Pi (Pin 1). The second pin of the sensor should be connected to a free GPIO pin on the Raspberry Pi (GPIO4, Pin 7 in my case) through a pull-up resistor (10kΩ used). The rightmost pin of the sensor goes to the GND pin on the Raspberry Pi (Pin 6). The second pin from the right on the sensor remains unused.
Please take a look at the pictures for details. 

### 4. Code

Create a Python file (here named `dht22_main.py`) and add the following code:

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

### 5. Output

![image](https://github.com/user-attachments/assets/3aee4118-032d-4f84-a1de-594d114e6ccc)

### 6. Improvements

The data could be transferred to a CSV file and transferred to a client automatically using cron daily. There, it can be plotted using pyplot.
