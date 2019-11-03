import time
import os
i = 0
while i != 3600:
    time.sleep(1)
    i+=1
print("You need to shut down the system now or else it will be automatically done in 10 seconds")
time.sleep(10)
print("going down")
os.system("shutdown now")
