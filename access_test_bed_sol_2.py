from queue import Queue
import threading
import time

testbeds = Queue()
testbeds.put("TB1")
testbeds.put("TB2")

def use_testbed(user):
    print(f"{user} waiting...")

    tb = testbeds.get()  # get available test bed
    print(f"{user} using {tb}")

    time.sleep(2)

    print(f"{user} releasing {tb}")
    testbeds.put(tb)


threads = []
for i in range(5):
    t = threading.Thread(target=use_testbed, args=(f"User-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()