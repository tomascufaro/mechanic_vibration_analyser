# Mechanic Vibration Analyser

## Overview

This repository contains a Python-based vibration analysis system that uses the **MPU6050** sensor to study and analyze vibration reduction in mechanical systems. The MPU6050 is a 6-axis motion tracking device that combines a 3-axis gyroscope and a 3-axis accelerometer, making it ideal for measuring vibrations and movements in various applications.

## Project Goal

The primary objective of this project is to collect, analyze, and visualize vibration data from mechanical systems to:
- Study vibration patterns in real-time
- Measure the effectiveness of vibration reduction techniques
- Provide data-driven insights for mechanical system optimization
- Enable remote monitoring of vibration data through network connectivity

## Features

- **Real-time Data Collection**: Capture accelerometer and gyroscope data from the MPU6050 sensor
- **Calibration Support**: Built-in calibration capabilities to improve measurement accuracy
- **Data Visualization**: Real-time plotting and animation of vibration data
- **Data Logging**: Save sensor readings to CSV files for further analysis
- **Remote Monitoring**: Client-server architecture for remote data access via socket communication
- **Multiple Measurement Modes**: Support for different accelerometer ranges (2g, 4g, 8g, 16g) and gyroscope ranges

## Repository Structure

```
.
├── mpu6050.py              # Core MPU6050 sensor interface class
├── data_writer.py          # Data logging utility for saving sensor readings
├── mpu_plot.py             # Real-time visualization and plotting
├── accel_calibration.csv   # Calibration data for accelerometer
└── socket/
    ├── rpi_server.py       # Server for Raspberry Pi to broadcast sensor data
    └── client_master.py    # Client to receive sensor data remotely
```

### File Descriptions

- **mpu6050.py**: Main sensor interface class that handles I2C communication with the MPU6050 sensor. Provides methods to read acceleration, gyroscope data, and temperature.

- **data_writer.py**: Command-line utility for continuous data collection. Supports calibration mode and raw data collection, saving readings to CSV files.

- **mpu_plot.py**: Creates real-time animated plots of accelerometer data (x, y, z axes) using matplotlib, useful for immediate visualization of vibration patterns.

- **socket/rpi_server.py**: Server application designed to run on a Raspberry Pi, broadcasting sensor data over the network.

- **socket/client_master.py**: Client application that receives sensor data from the server, enabling remote monitoring capabilities.

## Requirements

### Hardware
- MPU6050 sensor module
- Raspberry Pi or compatible board with I2C interface
- Proper wiring connections (SDA, SCL, VCC, GND)

### Software
- Python 3.x
- Required Python libraries:
  - `smbus` - For I2C communication
  - `pandas` - For data manipulation
  - `matplotlib` - For data visualization
  - `csv` - For data logging (standard library)
  - `socket` - For network communication (standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tomascufaro/mechanic_vibration_analyser.git
cd mechanic_vibration_analyser
```

2. Install required dependencies:
```bash
pip install pandas matplotlib

# For I2C communication, install one of the following:
# On Raspberry Pi/Debian/Ubuntu:
sudo apt-get install python3-smbus
# OR use smbus2 (cross-platform alternative):
pip install smbus2
```

3. Connect your MPU6050 sensor to the I2C pins on your device.

## Usage

### Basic Sensor Testing

Test the MPU6050 sensor connection:
```bash
python3 mpu6050.py
```

### Data Collection

Collect and save sensor data to a CSV file:
```bash
python3 data_writer.py
```

Options:
- `--cali`: Run calibration mode (saves to `accel_calibration.csv`)
- `--raw`: Collect raw data without calibration
- `--path <filename>`: Specify custom output file path

Examples:
```bash
# Calibration
python3 data_writer.py --cali

# Normal data collection with calibration
python3 data_writer.py --path my_data.csv

# Raw data collection
python3 data_writer.py --raw --path raw_data.csv
```

### Real-time Visualization

View live vibration data:
```bash
python3 mpu_plot.py
```

This will create:
- An animated plot showing real-time accelerometer data
- `medicion.gif` - Animated GIF of the measurement
- `medicion_last_frame.png` - Final frame capture

### Remote Monitoring

**On the Raspberry Pi (Server):**
```bash
python3 socket/rpi_server.py
```

**On the monitoring computer (Client):**
```bash
python3 socket/client_master.py
```

Note: Update the `HOST` variable in both files to match your network configuration.

## MPU6050 Sensor Information

The MPU6050 is a popular MEMS (Micro-Electro-Mechanical Systems) sensor that provides:

- **3-axis Accelerometer**: Measures linear acceleration
  - Configurable ranges: ±2g, ±4g, ±8g, ±16g
  - Used for vibration analysis and motion detection

- **3-axis Gyroscope**: Measures angular velocity
  - Configurable ranges: ±250°/s, ±500°/s, ±1000°/s, ±2000°/s
  - Useful for orientation tracking

- **Temperature Sensor**: Built-in temperature measurement

- **I2C Interface**: Simple two-wire communication protocol
  - Default address: 0x68

## Calibration

To improve measurement accuracy, calibrate the accelerometer before collecting data:

1. Place the sensor on a stable, level surface
2. Run calibration mode:
```bash
python3 data_writer.py --cali
```
3. Keep the sensor stationary for several seconds
4. The calibration offsets will be saved to `accel_calibration.csv`

The system will automatically apply these calibration values in subsequent measurements.

## Applications

This vibration analysis system can be used for:
- Monitoring mechanical equipment for predictive maintenance
- Testing vibration damping solutions
- Analyzing motor and engine vibrations
- Structural health monitoring
- Research in mechanical engineering and dynamics

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

Please check with the repository owner for licensing information.

## Author

Tomás Cufaro

## Acknowledgments

- MPU6050 datasheet and register documentation
- Python I2C libraries community
