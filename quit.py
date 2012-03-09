import os
import time

time.sleep(10)
os.system("killall mplayer")
os.system("python play.py")
