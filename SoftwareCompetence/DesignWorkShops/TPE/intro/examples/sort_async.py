import time, random
from concurrent.futures import ThreadPoolExecutor as TCE

TRIES=10
MAX=6

def taak(getal):
    time.sleep(getal)
    return getal, getal * getal

def demo():
    workers = TCE(max_workers=4)
    results = {}
    for n in range(TRIES):
        results[n] = workers.submit(taak, random.randint(1, MAX))
    for n, f in results.items():
        done = f.done()
        print("{n}: {g} ==> {r} ({done})".format(n=n, g=f.result()[0], r=f.result()[1],  done="direct" if done else "waited"))

if __name__ == '__main__':
    demo()
