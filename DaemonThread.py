from threading import *
def display():
    print("This is display method")
    t2=Thread(target=demo)
    print("Demon nature of t2 is:",t2.daemon)
def demo():
    print("Somrthing")

t1=Thread(target=display)
print("Before",t1.daemon)
t1.daemon=True
print("After",t1.daemon)
t1.start()

print("This is main thread")