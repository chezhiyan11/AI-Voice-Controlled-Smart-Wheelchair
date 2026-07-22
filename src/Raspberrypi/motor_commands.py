import serial
import time

# UART Communication (Recommended for reliability)
ser = serial.Serial('/dev/serial0', 115200, timeout=1)
time.sleep(2)

def send_command(cmd):
    command_map = {
        "forward": "FORWARD",
        "backward": "BACKWARD",
        "left": "LEFT",
        "right": "RIGHT",
        "stop": "STOP"
    }
    msg = command_map.get(cmd, cmd.upper()) + "\n"
    ser.write(msg.encode())
    print(f"Sent to ESP32: {msg.strip()}")