import os
import time
from utils import log_event

# Terminal sound (cross-platform)
def beep():
    try:
        # Linux/Mac terminal bell
        print("\a", end="")
    except:
        pass

def flash_alert(message: str):
    """Simple safe visual alert"""
    print("\n" + "!" * 60)
    print(f"   ALERT: {message}")
    print("!" * 60 + "\n")

def send_alert(message: str):
    """
    Full alert system:
    - Log event
    - Terminal flash
    - Sound beep
    """
    log_event(f"ALERT: {message}")
    flash_alert(message)
    beep()
