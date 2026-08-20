import time
from datetime import datetime
print("Press Ctrl+C to stop")
try:
    while True:
        print("\rTime:", datetime.now().strftime("%H:%M:%S"), end="", flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped.")
