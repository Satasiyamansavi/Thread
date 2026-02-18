from threading import Thread
import time
def display():
    print("Welcome in office!")
def show():
    print("Thank you!")
start=time.time()
print("Starting time:",start)
t1=Thread(target=display)
t2=Thread(target=show)
t1.start()
t2.start()
t1.join()
t2.join()
print("Ending time:",time.time())
print("Total compeletion time:",time.time()-start)
