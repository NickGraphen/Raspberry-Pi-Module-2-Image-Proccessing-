import os

import time



count = 0

while count>-1:
        ts = time.time()
        readable = time.ctime(ts)
        temp = os.popen("vcgencmd measure_temp").readline()

        print(count), "SECONDS"
        print(temp) + (readable)
        print "____________________"
        count+=10
        time.sleep(10);
