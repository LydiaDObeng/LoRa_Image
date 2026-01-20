# LoRa Image Transmission System

A Python-based implementation for transmitting images wirelessly using LoRa SX127x modules on Raspberry Pi. This project demonstrates long-range, low-power image transmission with performance metrics including RSSI, SNR, BER, and packet reception rate.

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Hardware Requirements](#-hardware-requirements)
- [Software Requirements](#-software-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Performance Metrics](#-performance-metrics)
- [Configuration](#-configuration)
- [Project Structure](#-project-structure)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Publications](#-publications)

## 🎯 Overview

This system enables wireless image transmission over long distances using LoRa (Long Range) technology. Images are compressed using JPEG encoding, split into chunks, and transmitted via LoRa modules operating at 915 MHz. The receiver reconstructs the image and calculates communication quality metrics.

### Key Capabilities

- **Long-range transmission**: Utilizes LoRa's sub-GHz ISM band for extended range
- **Low power consumption**: Efficient power management with sleep modes
- **JPEG compression**: Reduces bandwidth requirements while maintaining image quality
- **Real-time metrics**: Monitors RSSI, SNR, BER, and packet reception rate
- **Robust transmission**: Chunk-based transmission with end-of-transmission markers

## ✨ Features

### Transmitter Features
- JPEG image compression with configurable quality
- Automatic image chunking (240 bytes per packet)
- Progress monitoring during transmission
- Power-efficient sleep modes between transmissions
- End-of-transmission marker for reliable completion detection

### Receiver Features
- Continuous reception mode
- Real-time RSSI monitoring
- Signal-to-Noise Ratio (SNR) calculation
- Bit Error Rate (BER) analysis
- Packet Reception Rate (PRR) measurement
- Automatic image reconstruction and saving

## 🔧 Hardware Requirements

### Essential Components

1. **Raspberry Pi** (tested on Pi 3B+/4)
   - Any model with GPIO pins
   - Running Raspbian/Raspberry Pi OS

2. **LoRa SX127x Modules** (2 units - one for TX, one for RX)
   - SX1276/SX1277/SX1278/SX1279
   - Operating frequency: 915 MHz (configurable)
   - Recommended modules:
     - HopeRF RFM95W
     - Dragino LoRa GPS HAT
     - Adafruit RFM95W

3. **Antennas**
   - 915 MHz compatible antennas
   - Recommended: 3dBi or higher gain

4. **Power Supply**
   - Stable 5V power for Raspberry Pi
   - Optional: Battery pack for mobile deployments

### Wiring Connections

| SX127x Pin | RPi GPIO Pin | Pin Number |
|------------|--------------|------------|
| VCC        | 3.3V         | 1 or 17    |
| GND        | GND          | 6, 9, 14, 20, 25, 30, 34, 39 |
| SCK        | GPIO11 (SCLK)| 23         |
| MISO       | GPIO9 (MISO) | 21         |
| MOSI       | GPIO10 (MOSI)| 19         |
| NSS/CS     | GPIO8 (CE0)  | 24         |
| RESET      | GPIO25       | 22         |
| DIO0       | GPIO4        | 7          |

**Important**: Verify your specific LoRa module's pinout as it may vary by manufacturer.

## 💻 Software Requirements

### Operating System
- Raspberry Pi OS (formerly Raspbian)
- Tested on Buster and Bullseye

### Python Version
- Python 3.6 or higher

### Required Libraries
```
RPi.GPIO
spidev
Pillow (PIL)
pyLoRa (SX127x library)
```

## 📥 Installation

### 1. System Preparation

Update your Raspberry Pi:
```bash
sudo apt-get update
sudo apt-get upgrade
```

### 2. Enable SPI Interface

```bash
sudo raspi-config
```
Navigate to: **Interface Options** → **SPI** → **Enable**

Reboot:
```bash
sudo reboot
```

### 3. Install Python Dependencies

```bash
# Install pip if not already installed
sudo apt-get install python3-pip

# Install required packages
pip3 install RPi.GPIO
pip3 install spidev
pip3 install Pillow
```

### 4. Install SX127x LoRa Library

The SX127x library is included in this repository. If installing separately:

```bash
git clone https://github.com/mayeranalytics/pySX127x.git
cd pySX127x
sudo python3 setup.py install
```

### 5. Clone This Repository

```bash
git clone https://github.com/LydiaDObeng/LoRa_Image.git
cd LoRa_Image/Image_Transmission_LoRa
```

### 6. Prepare Your Image

Place your image file in the same directory:
```bash
# Rename your image or update the code to match your filename
cp /path/to/your/image.jpg Image1.jpg
```

## 🚀 Usage

### Running the Transmitter

On the Raspberry Pi configured as the transmitter:

```bash
cd Image_Transmission_LoRa
sudo python3 Image_Transmitter.py
```

**Expected Output:**
```
915.0
[chunk data...]
[chunk data...]
...
Sending Completed
```

### Running the Receiver

On the Raspberry Pi configured as the receiver:

```bash
cd Image_Transmission_LoRa
sudo python3 Image_Receiver.py
```

**Expected Output:**
```
RSSI: -45.2
RSSI: -46.8
...
Bit Error Rate (BER): 0.001
% of Correct Packets: 99.900
Image saved as ReceivedJ1.jpg
Average RSSI: -45.67
SNR: 77.230
```

### Graceful Shutdown

Press `Ctrl+C` to stop either script. The cleanup routines will:
- Set LoRa module to sleep mode
- Release GPIO resources
- Close SPI connections

## 📊 Performance Metrics

The receiver calculates and displays several important metrics:

### 1. **RSSI (Received Signal Strength Indicator)**
- Measured in dBm
- Typical range: -30 dBm (excellent) to -120 dBm (poor)
- Real-time monitoring for each packet
- Average calculated across all packets

### 2. **SNR (Signal-to-Noise Ratio)**
- Calculated as: SNR = RSSI - Noise Floor
- Noise floor assumed at -122.9 dBm
- Higher values indicate better signal quality
- Typical good SNR: >10 dB

### 3. **BER (Bit Error Rate)**
- Ratio of incorrect bits to total bits
- Calculated by comparing transmitted and received images
- Lower is better (0.0 = perfect)
- Formula: `BER = error_bits / total_bits`

### 4. **PRR (Packet Reception Rate)**
- Percentage of correctly received packets
- Calculated as: `PRR = (1 - BER) × 100`
- Values approaching 100% indicate reliable transmission

**Note**: For accurate BER/PRR calculation, ensure the original image (`Image1.jpg`) is present in the `pics/` directory on the receiver.

## ⚙️ Configuration

### Frequency Configuration

Default frequency: **915 MHz** (ISM band for North America)

To change frequency, edit both files:

**Image_Transmitter.py:**
```python
self.set_freq(915.0)  # Change to your desired frequency
```

**Image_Receiver.py:**
```python
self.set_freq(915.0)  # Must match transmitter frequency
```

**Regional Frequency Bands:**
- North America: 915 MHz
- Europe: 868 MHz
- Asia: 433 MHz or 923 MHz

### Compression Quality

Adjust JPEG quality in `Image_Transmitter.py`:
```python
image.save(image_stream, format='JPEG', quality=85)
# Range: 1-100
# Higher = better quality, larger file size
# Lower = lower quality, smaller file size, faster transmission
```

### Chunk Size

Modify transmission chunk size:
```python
chunk_size = 240  # bytes per packet
# Maximum: 255 bytes (LoRa limitation)
# Smaller chunks = more reliable but slower
# Larger chunks = faster but may lose data
```

### Transmission Delay

Adjust delay between chunks:
```python
sleep(1)  # seconds between packets
# Increase for more reliable transmission
# Decrease for faster transmission
```

## 📁 Project Structure

```
LoRa_Image/
├── README.md                          # This file
├── LICENSE                            # GNU General Public License
└── Image_Transmission_LoRa/
    ├── Image_Transmitter.py          # Transmitter script
    ├── Image_Receiver.py             # Receiver script
    ├── Image1.jpg                    # Sample input image (user-provided)
    ├── ReceivedJ1.jpg               # Output received image
    ├── pics/                         # Directory for BER comparison
    │   └── Image1.jpg               # Original image for BER calculation
    └── SX127x/                       # LoRa driver library
        ├── __init__.py
        ├── LoRa.py                   # Main LoRa class
        ├── board_config.py           # GPIO configuration
        ├── constants.py              # LoRa constants
        └── LoRaArgumentParser.py     # Command-line argument parser
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. **"RuntimeError: No access to /dev/mem"**
**Solution**: Run scripts with `sudo`
```bash
sudo python3 Image_Transmitter.py
```

#### 2. **"OSError: [Errno 121] Remote I/O error"**
**Possible causes**:
- SPI not enabled
- Incorrect wiring
- Faulty LoRa module

**Solutions**:
```bash
# Verify SPI is enabled
lsmod | grep spi
# Should show: spi_bcm2835

# Check SPI devices
ls -l /dev/spi*
# Should show: /dev/spidev0.0 and /dev/spidev0.1
```

#### 3. **"Image not received completely"**
**Solutions**:
- Increase transmission delay: `sleep(2)`
- Reduce chunk size: `chunk_size = 200`
- Check antenna connections
- Verify both devices are on same frequency
- Reduce distance between modules for testing

#### 4. **"High BER or low PRR"**
**Solutions**:
- Improve antenna placement (vertical, elevated)
- Reduce obstacles between transmitter and receiver
- Check for interference from other 915 MHz devices
- Increase transmission power (if supported by module)

#### 5. **"ModuleNotFoundError: No module named 'SX127x'"**
**Solution**: Install the SX127x library
```bash
cd pySX127x
sudo python3 setup.py install
```

#### 6. **GPIO Warnings**
**Solution**: Warnings are suppressed in code, but if persistent:
```python
GPIO.setwarnings(False)  # Already in code
# Or manually cleanup before running
sudo python3 -c "import RPi.GPIO as GPIO; GPIO.cleanup()"
```

## 🧪 Testing

### Quick Test Procedure

1. **Test LoRa Modules**:
   ```bash
   # On transmitter
   sudo python3 -c "from SX127x.LoRa import LoRa; print('TX OK')"
   
   # On receiver
   sudo python3 -c "from SX127x.LoRa import LoRa; print('RX OK')"
   ```

2. **Test Image Loading**:
   ```python
   from PIL import Image
   img = Image.open("Image1.jpg")
   print(f"Image size: {img.size}")
   ```

3. **Short-Range Test**:
   - Place modules 1-2 meters apart
   - Use small test image (< 100 KB)
   - Verify successful transmission
   - Gradually increase distance

4. **Performance Benchmark**:
   ```bash
   # Test different image sizes
   # Small: 50 KB
   # Medium: 200 KB  
   # Large: 500 KB
   # Measure transmission time and quality
   ```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Ideas for Contributions

- Add support for multiple image formats (PNG, BMP)
- Implement error correction codes
- Add GUI interface
- Support for video transmission
- Encryption for secure transmission
- Adaptive transmission rate based on signal quality
- Web-based monitoring dashboard
- Support for other LoRa modules (RFM96, etc.)

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## 📚 Publications

This work has been presented at:

**IEEE Consumer Communications & Networking Conference (CCNC) 2024**
- Title: *Image Transmission over LoRa-Based Networks: A Performance Study Using Image Compression and Reconstruction Methods*
- DOI: [10.1109/CCNC51664.2024.10454687](https://ieeexplore.ieee.org/abstract/document/10454687)
- Full Paper: [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/10454687)

## 👩‍💻 Author

**Lydia D. Obeng**
- GitHub: [@LydiaDObeng](https://github.com/LydiaDObeng)
- LinkedIn: [Lydia D. Obeng](https://www.linkedin.com/in/lydia-obeng/)

## 🙏 Acknowledgments

- [pySX127x](https://github.com/mayeranalytics/pySX127x) for the LoRa driver library
- Raspberry Pi Foundation for excellent documentation
- LoRa Alliance for the LoRaWAN specification

## 📞 Support

If you encounter issues or have questions:

1. Check the [Troubleshooting](#troubleshooting) section
2. Search [existing issues](https://github.com/LydiaDObeng/LoRa_Image/issues)
3. Create a [new issue](https://github.com/LydiaDObeng/LoRa_Image/issues/new) with:
   - Detailed description
   - Error messages
   - Hardware setup
   - Steps to reproduce

---

**⭐ If you find this project useful, please consider giving it a star!**

Last Updated: January 2026