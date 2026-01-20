# LoRa Image Transmission Configuration
# Copy this file to config.py and modify as needed

# ===========================
# LoRa Radio Configuration
# ===========================

# Operating Frequency (MHz)
# North America: 915.0
# Europe: 868.0
# Asia: 433.0 or 923.0
FREQUENCY = 915.0

# Transmission Power (dBm)
# Range: 2-20 dBm (depends on module)
# Higher power = longer range but more power consumption
TX_POWER = 17

# Spreading Factor
# Range: 7-12
# Higher SF = longer range but slower transmission
# SF7 = fastest, shortest range
# SF12 = slowest, longest range
SPREADING_FACTOR = 7

# Bandwidth (Hz)
# Options: 7800, 10400, 15600, 20800, 31250, 41700, 62500, 125000, 250000
# Higher bandwidth = faster transmission but shorter range
BANDWIDTH = 125000

# Coding Rate
# Options: 5, 6, 7, 8 (represents 4/5, 4/6, 4/7, 4/8)
# Higher rate = more error correction but slower
CODING_RATE = 5

# ===========================
# Image Configuration
# ===========================

# Input Image Path (Transmitter)
INPUT_IMAGE = "Image1.jpg"

# Output Image Path (Receiver)
OUTPUT_IMAGE = "ReceivedJ1.jpg"

# JPEG Compression Quality (1-100)
# Higher quality = larger file size
JPEG_QUALITY = 85

# Chunk Size (bytes per packet)
# Maximum: 255 bytes
# Recommended: 200-240 bytes
CHUNK_SIZE = 240

# ===========================
# Transmission Configuration
# ===========================

# Delay between packet transmissions (seconds)
# Increase for more reliable transmission
# Decrease for faster transmission
TRANSMISSION_DELAY = 1.0

# Maximum Retransmission Attempts
MAX_RETRIES = 3

# Timeout for acknowledgment (seconds)
ACK_TIMEOUT = 2.0

# End-of-transmission marker
# Must be unique bytes not in image data
EOT_MARKER = [0x41, 0x42, 0x43]  # "ABC"

# ===========================
# Performance Monitoring
# ===========================

# Calculate BER (requires original image on receiver)
CALCULATE_BER = True

# Original image path for BER calculation (Receiver)
BER_REFERENCE_IMAGE = "pics/Image1.jpg"

# Assumed noise floor for SNR calculation (dBm)
NOISE_FLOOR = -122.9

# ===========================
# GPIO Pin Configuration
# ===========================
# These match the SX127x library defaults
# Only modify if using custom wiring

# SPI Chip Select
CS_PIN = 8  # GPIO8 (CE0)

# Reset Pin
RESET_PIN = 25  # GPIO25

# DIO0 Pin (for interrupt)
DIO0_PIN = 4  # GPIO4

# ===========================
# Debug Configuration
# ===========================

# Enable verbose logging
VERBOSE = False

# Print RSSI values
PRINT_RSSI = True

# Print each transmitted chunk
PRINT_CHUNKS = False

# Save transmission statistics
SAVE_STATS = True

# Statistics output file
STATS_FILE = "transmission_stats.csv"

# ===========================
# Advanced Settings
# ===========================

# Preamble Length (symbols)
PREAMBLE_LENGTH = 8

# Enable CRC
ENABLE_CRC = True

# Low Data Rate Optimize
# Enable for SF11 and SF12 at 125kHz bandwidth
LOW_DATA_RATE_OPTIMIZE = False

# AGC Auto On
AGC_AUTO = True

# ===========================
# Usage Notes
# ===========================
# 1. Ensure FREQUENCY matches your local regulations
# 2. Both transmitter and receiver must use identical settings
# 3. Test with short distances first, then increase
# 4. Higher SF = better range but slower speed
# 5. Adjust TRANSMISSION_DELAY based on your needs
