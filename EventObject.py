import threading
import time
e1=threading.Event()
def demo():
    print("Demo Lecture 1 started")
    time.sleep(2)
    e1.set()
def demo1():
    e1.wait()
    if e1.is_set():
       print("Demo Lecture 2 started") 
t1=threading.Thread(target=demo)
t2=threading.Thread(target=demo1)
t1.start()
t2.start()