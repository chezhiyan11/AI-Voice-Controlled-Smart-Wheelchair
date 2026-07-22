from voice_control import listen_command
from motor_commands import send_command
from ai_navigation import start_ai_navigation
import time

print("🚀 Voice-Controlled Smart Wheelchair System Started")

while True:
    command = listen_command()
    
    if command:
        if "forward" in command:
            send_command("forward")
        elif "backward" in command:
            send_command("backward")
        elif "left" in command:
            send_command("left")
        elif "right" in command:
            send_command("right")
        elif "stop" in command:
            send_command("stop")
        elif "auto" in command or "ai" in command:
            start_ai_navigation()
    
    time.sleep(0.3)