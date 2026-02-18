from threading import *
from time import sleep  
obj=Semaphore()
def demo(name):
    obj.acquire()
    for i in range(3):
        print("Hello")
        print(name)
        sleep(0.5)
    obj.release()
t1=Thread(target=demo,args=("Thread-1",))
t2=Thread(target=demo,args=("Thread-2",))
t3=Thread(target=demo,args=("Thread-3",))
t4=Thread(target=demo,args=("Thread-4",))
t5=Thread(target=demo,args=("Thread-5",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()