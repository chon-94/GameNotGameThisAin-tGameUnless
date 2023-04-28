import time

while True:
    for i in range(39):
        print(".", end="<>", flush=True)
        time.sleep(0.025)
    print("+", flush=True)
