import time

# this is not the way to check the time 
start = time.time()
print(start)
for i in range(500):
    print(i, end=", ")
    
print()
time.sleep(2)

print(time.time() - start)