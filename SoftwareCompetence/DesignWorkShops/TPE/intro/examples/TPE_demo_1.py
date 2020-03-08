#! python
import time, random
from concurrent.futures import ThreadPoolExecutor as TCE

TRIES=10
MAX=6

def taak(getal):
    time.sleep(getal/MAX)         # Simulate a complicated calculations ...
    return getal, getal * getal   #  ... returning the number and it square


def demo():
    workers = TCE(max_workers=4)   # (1)
    results = {}

    for n in range(TRIES):        # (2) Submit all tasks;  (with random number)
        results[n] = workers.submit(taak, random.randint(1, MAX)) # Store the Futures

    for n, f in results.items(): #  (3) Print the results (in order)
        done = f.done()
        print("{n}: {g} ==> {r} ({done})".format(n=n, g=f.result()[0], r=f.result()[1],
                                                 done="direct" if done else "waited"))

if __name__ == '__main__':
    demo()
