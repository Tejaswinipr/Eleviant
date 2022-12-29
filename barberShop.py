
import threading,time,random
from queue import Queue

bench = []

def addCusToQ(cust):
    if len(bench)<5:
        bench.append(cust)
        print(bench)

def barber1():
    while True:
        try:
            t=random.randint(10,60)
            time.sleep(t)
            print("Barber1:",bench[0])
            bench.remove(bench[0])
        except:
            pass

def barber2():
    while True:
        try:
            t=random.randint(10,60)
            time.sleep(t)
            print("Barber2:",bench[0])
            bench.remove(bench[0])
        except:
            pass

def customers():
    c=1
    cust=""
    while True:
        t=random.randint(1,5)
        time.sleep(t)
        cust="customer"+str(c)
        c+=1
        addCusToQ(cust)


threading.Thread(target=customers).start()

threading.Thread(target=barber1).start()
threading.Thread(target=barber2).start()




