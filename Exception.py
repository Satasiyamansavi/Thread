import threading
import time
def exception_hook(args):
    print("To Handle Exception")
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
def display():
    for i in range(3):
        print("Hello"+10)
def demo():
    for i in range(3):
        print("Welcome!")
threading.excepthook=exception_hook
t1=threading.Thread(target=display)
t2=threading.Thread(target=demo)
t1.start()
t2.start()
t1.join()
t2.join()
for i in range(3):
    time.sleep(2)
    print("My dear student")