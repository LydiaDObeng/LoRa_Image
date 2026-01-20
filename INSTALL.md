# Installation Guide

Complete step-by-step installation guide for the LoRa Image Transmission System.

## Table of Contents

1. [Hardware Setup](#hardware-setup)
2. [Raspberry Pi OS Setup](#raspberry-pi-os-setup)
3. [Software Installation](#software-installation)
4. [LoRa Module Connection](#lora-module-connection)
5. [Testing Installation](#testing-installation)
6. [Troubleshooting](#troubleshooting)

## Hardware Setup

### Required Components

#### For Each Device (Transmitter & Receiver)

- **Raspberry Pi** (any model with 40-pin GPIO)
  - Raspberry Pi 4B (recommended)
  - Raspberry Pi 3B/3B+
  - Raspberry Pi Zero W/WH

- **LoRa Module**: SX127x series
  - RFM95W (recommended)
  - RFM96W
  - RFM98W
  - SX1276/77/78/79 based modules

- **Antenna**: Appropriate for your frequency
  - 915 MHz: 86mm quarter-wave antenna
  - 868 MHz: 87mm quarter-wave antenna
  - External antenna recommended for better range

- **Power Supply**
  - 5V 2.5A+ for Raspberry Pi 3/4
  - 5V 3A+ for Raspberry Pi 4 (recommended)

- **microSD Card**
  - 16GB minimum
  - Class 10 or better

### Optional Components

- Breadboard or prototyping HAT
- Jumper wires (female-to-female)
- Heat sinks for Raspberry Pi (if running continuously)
- Case for weather protection (outdoor deployments)

## Raspberry Pi OS Setup

### 1. Download Raspberry Pi OS

Download from: https://www.raspberrypi.org/software/

**Recommended**: Raspberry Pi OS Lite (64-bit) or Full

### 2. Write Image to SD Card

**Using Raspberry Pi Imager** (recommended):
```bash
# Download and install Raspberry Pi Imager
# Select OS: Raspberry Pi OS (other) → Raspberry Pi OS Lite
# Select SD card
# Configure settings (hostname, SSH, WiFi)
# Write
```

**Using Command Line** (Linux/Mac):
```bash
# Find SD card device
lsblk

# Write image (replace /dev/sdX with your SD card)
sudo dd if=2024-xx-xx-raspios-bookworm-arm64-lite.img of=/dev/sdX bs=4M status=progress
sudo sync
```

### 3. Enable SSH (if not using Imager)

```bash
# Mount boot partition
cd /media/YOUR_USERNAME/boot

# Create empty ssh file
touch ssh

# Optional: Configure WiFi
cat > wpa_supplicant.conf << EOF
country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="YOUR_WIFI_SSID"
    psk="YOUR_WIFI_PASSWORD"
}
EOF
```

### 4. First Boot

Insert SD card and power on Raspberry Pi.

Default credentials:
- Username: `pi`
- Password: `raspberry` (change immediately!)

SSH into your Pi:
```bash
ssh pi@raspberrypi.local
# or
ssh pi@<IP_ADDRESS>
```

### 5. Initial Configuration

```bash
# Update system
sudo apt-get update
sudo apt-get upgrade -y

# Change default password
passwd

# Optional: Configure timezone, locale, etc.
sudo raspi-config
```

## Software Installation

### 1. Install System Dependencies

```bash
# Update package list
sudo apt-get update

# Install Python and pip
sudo apt-get install -y python3 python3-pip python3-dev

# Install git
sudo apt-get install -y git

# Install SPI and I2C tools
sudo apt-get install -y python3-spidev
```

### 2. Enable SPI Interface

**Method 1: Using raspi-config**
```bash
sudo raspi-config
```
Navigate to:
- `Interface Options` → `SPI` → `Yes` → `OK` → `Finish`

**Method 2: Edit config.txt**
```bash
sudo nano /boot/config.txt

# Add or uncomment this line:
dtparam=spi=on

# Save (Ctrl+O) and exit (Ctrl+X)
sudo reboot
```

### 3. Verify SPI is Enabled

After reboot:
```bash
# Check for SPI modules
lsmod | grep spi

# Expected output:
# spi_bcm2835

# Check for SPI devices
ls -l /dev/spi*

# Expected output:
# /dev/spidev0.0
# /dev/spidev0.1
```

### 4. Install Python Libraries

```bash
# Install RPi.GPIO
sudo pip3 install RPi.GPIO

# Install spidev
sudo pip3 install spidev

# Install Pillow (image processing)
sudo pip3 install Pillow

# Verify installations
python3 -c "import RPi.GPIO; import spidev; from PIL import Image; print('All modules imported successfully')"
```

### 5. Install SX127x LoRa Library

**Option A: Use included library** (recommended)
```bash
# Clone this repository
git clone https://github.com/LydiaDObeng/LoRa_Image.git
cd LoRa_Image/Image_Transmission_LoRa
# Library is in SX127x/ directory
```

**Option B: Install from source**
```bash
# Clone pySX127x library
git clone https://github.com/mayeranalytics/pySX127x.git
cd pySX127x

# Install
sudo python3 setup.py install

# Verify
python3 -c "from SX127x.LoRa import LoRa; print('LoRa library installed')"
```

### 6. Clone This Repository

If you haven't already:
```bash
cd ~
git clone https://github.com/LydiaDObeng/LoRa_Image.git
cd LoRa_Image
```

## LoRa Module Connection

### Wiring Diagram

```
LoRa SX127x Module          Raspberry Pi
─────────────────          ──────────────
VCC (3.3V)         ───────→ Pin 1 or 17 (3.3V)
GND                ───────→ Pin 6 (GND)
MISO               ───────→ Pin 21 (GPIO 9)
MOSI               ───────→ Pin 19 (GPIO 10)
SCK                ───────→ Pin 23 (GPIO 11)
NSS/CS             ───────→ Pin 24 (GPIO 8)
RESET              ───────→ Pin 22 (GPIO 25)
DIO0               ───────→ Pin 7 (GPIO 4)
DIO1               ───────→ Not connected
DIO2               ───────→ Not connected
```

### Connection Steps

1. **Power off Raspberry Pi** before connecting

2. **Connect LoRa module** using the diagram above

3. **Attach antenna** to the LoRa module
   - **CRITICAL**: Never power on without antenna connected
   - Can damage the RF amplifier

4. **Double-check connections**
   - Verify voltage: LoRa modules use **3.3V, NOT 5V**
   - Incorrect voltage will damage the module

5. **Power on** Raspberry Pi

### Verification

Test GPIO connections:
```bash
# Test script
python3 << EOF
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# Test pins
test_pins = [4, 8, 25]
GPIO.setup(test_pins, GPIO.OUT)
for pin in test_pins:
    GPIO.output(pin, GPIO.HIGH)
    GPIO.output(pin, GPIO.LOW)

GPIO.cleanup()
print("GPIO test completed successfully")
EOF
```

## Testing Installation

### 1. Test LoRa Module Detection

Create test script:
```bash
cd ~/LoRa_Image/Image_Transmission_LoRa

cat > test_lora.py << 'EOF'
from SX127x.LoRa import LoRa
from SX127x.board_config import BOARD
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
BOARD.setup()

class TestLoRa(LoRa):
    def __init__(self):
        super(TestLoRa, self).__init__(verbose=False)
        self.set_mode(MODE.SLEEP)
        self.set_freq(915.0)
        print(f"Frequency set to: {self.get_freq()} MHz")
        print("LoRa module detected successfully!")

try:
    lora = TestLoRa()
except Exception as e:
    print(f"Error: {e}")
finally:
    BOARD.teardown()
EOF

# Run test
sudo python3 test_lora.py
```

**Expected output**:
```
Frequency set to: 915.0 MHz
LoRa module detected successfully!
```

### 2. Test Image Loading

```bash
# Create test image or copy your image
cp /path/to/test/image.jpg Image1.jpg

# Test image loading
python3 << EOF
from PIL import Image
import os

if os.path.exists("Image1.jpg"):
    img = Image.open("Image1.jpg")
    print(f"Image loaded successfully!")
    print(f"Size: {img.size}")
    print(f"Format: {img.format}")
else:
    print("Please provide Image1.jpg")
EOF
```

### 3. Quick Transmission Test

**On Transmitter**:
```bash
# Use a small test image first
sudo python3 Image_Transmitter.py
```

**On Receiver** (on another Pi):
```bash
sudo python3 Image_Receiver.py
```

## Troubleshooting

### SPI Issues

**Problem**: `OSError: [Errno 2] No such file or directory: '/dev/spidev0.0'`

**Solution**:
```bash
# Enable SPI
sudo raspi-config
# Interface Options → SPI → Enable
sudo reboot

# Verify
ls -l /dev/spi*
```

### Permission Issues

**Problem**: `RuntimeError: No access to /dev/mem`

**Solution**: Run with sudo:
```bash
sudo python3 Image_Transmitter.py
```

### Module Import Errors

**Problem**: `ModuleNotFoundError: No module named 'SX127x'`

**Solution**:
```bash
# Reinstall library
cd ~/pySX127x
sudo python3 setup.py install

# Or use the included library
cd ~/LoRa_Image/Image_Transmission_LoRa
# Make sure you're in the right directory
```

### LoRa Module Not Detected

**Problem**: `OSError: [Errno 121] Remote I/O error`

**Checklist**:
1. Verify all wire connections
2. Check module is powered (3.3V)
3. Ensure SPI is enabled
4. Try different GPIO pins
5. Test with multimeter (continuity)
6. Replace module if faulty

### Image Not Received

**Checklist**:
1. Both devices on same frequency
2. Antennas properly connected
3. Reduce distance for testing
4. Check for interference
5. Verify transmission completed
6. Check receiver logs

## Next Steps

After successful installation:

1. Read the [README.md](README.md) for usage instructions
2. Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
3. Review configuration options in `config_example.py`
4. Experiment with different settings
5. Test at various distances

## Additional Resources

- [Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/)
- [LoRa Alliance](https://lora-alliance.org/)
- [SX127x Datasheet](https://www.semtech.com/products/wireless-rf/lora-transceivers)
- [pySX127x Library](https://github.com/mayeranalytics/pySX127x)

## Support

If you encounter issues:
1. Check this guide thoroughly
2. Review README troubleshooting section
3. Search existing GitHub issues
4. Create new issue with detailed information

---

Installation guide last updated: January 2026
