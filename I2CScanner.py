import smbus

bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1

for device in range(128):
  try:
    bus.read_byte(device)
    print(f"Found device at: 0x{device:02x}")
  except:
    pass