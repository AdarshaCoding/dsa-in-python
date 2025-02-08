import time

start = time.time()
for i in range(1, 5):
    time.sleep(1)
    print(i)

print("\n", time.time() - start)
