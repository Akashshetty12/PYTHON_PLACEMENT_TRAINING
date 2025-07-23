import time
import sys
h = 12
m = 59
s=40
while True:
    sys.stdout.write(f"\r{h:02d}:{m:02d}:{s:02d}")
    sys.stdout.flush()
    time.sleep(1)
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 13:
        h = 1
        m = 0
        s = 0