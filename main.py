import time

print("\n")
print("{:3d}".format(0), end="   ")
for i in range(10):
    print("{:3d}".format(i+1), end="   ")
    if i + 1 == 10 : 
        print("\n","_______________________________________________________________", end="\n"*2)

for i in range(10):
    for j in range(10):
        if j == 0:
            print("{:3d}".format(i+1), end=" | ")
        else: 
            time.sleep(0.1)
        print("{:3d}".format((i+1)*(j+1)), end="   ", flush=True)
        if j+1 == 10:
            print("\n")        