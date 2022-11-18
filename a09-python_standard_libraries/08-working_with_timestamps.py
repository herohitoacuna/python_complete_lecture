# ************ WORKING WITH TIMESTAMPS ******************
import time         # gives us timestamps
# import datetime     # gives us "date_time object" with attribute year, month, day

# print(time.time())
# result: 1668767376.621522 in second, since the beginning of time in my computer


def send_emails():
    for i in range(1000):
        pass


# the result of time.time() can be used to perform certain calculation
start = time.time()
send_emails()
end = time.time()
duration = end - start
print(duration)
