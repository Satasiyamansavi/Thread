import threading
from time import sleep
e1=threading.Event()
def signal_light():
    while True:
        print("Light is green")
        e1.set()
        sleep(3)
        print("Light is red")
        e1.clear()
        sleep(3)
        e1.set()

def signal_msg():
    e1.wait()
    while e1.is_set():
        print("You can go")
        sleep(0.5)
        e1.wait()

t1=threading.Thread(target=signal_light)
t2=threading.Thread(target=signal_msg)
t1.start()
t2.start()