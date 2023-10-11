from datetime import datetime
import time

f = open("log.txt", "a") # może być w lub a

for i in range(0, 10):
    print(datetime.now().strftime("%Y - %m - %d %H:%M:%S - "), i) # tutaj jest łańcuch metod now i strftime
    f.write(datetime.now().strftime("%Y - %m - %d %H:%M:%S - "))
    time.sleep(1) # opóźniacz o 1 sekundę
    f.write(str(i))
    f.write("\n")
f.close()
