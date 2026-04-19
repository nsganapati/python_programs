from queue import Queue
import threading
import time

testbeds = Queue()
testbeds.put("TB1")
testbeds.put("TB2")

def use_testbed(user):
    """
    Simulates a user attempting to acquire, use, and release a test bed.
    
    This function uses a Queue to manage available test beds. A user will wait
    until a test bed (TB1 or TB2) is available in the queue, use it, and then
    return it back to the queue for others to use.
    
    Args:
        user (str): The name or identifier of the user trying to access a test bed.
    """
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