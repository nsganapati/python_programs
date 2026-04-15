import threading
import time
import random

# Only 2 test beds available
testbed_semaphore = threading.Semaphore(2)

def use_testbed(user):
    print(f"{user} is waiting for a test bed...")

    # acquire test bed
    with testbed_semaphore:
        print(f"{user} got a test bed ✅")

        # simulate work
        time.sleep(random.randint(1, 3))

        print(f"{user} released the test bed ❌")


# 5 users
users = [f"User-{i}" for i in range(1, 6)]

threads = []

for user in users:
    t = threading.Thread(target=use_testbed, args=(user,))
    threads.append(t)
    t.start()

# wait for all to finish
for t in threads:
    t.join()

