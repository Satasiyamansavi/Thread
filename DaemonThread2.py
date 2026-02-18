from threading import *
from time import *
def demo():
    for i in range(5):
        print("Lecture ",i)
        sleep(0.5)
t1=Thread(target=demo)
t1.daemon=True
t1.start()
sleep(3)
print("Lecture start")
print("Lecture over!")