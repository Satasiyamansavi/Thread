from threading import Thread
import os
def display():
    print("Disply Method")
def show():
    print("Show Method")
t1=Thread(target=display)
t2=Thread(target=show)
t1.start()
t2.start()
print(t1.ident)
print(t1.native_id)
print(os.getpid())