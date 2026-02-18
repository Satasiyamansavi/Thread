import threading
def display():
    for i in range(3):
        print("Hello")
timer=threading.Timer(5,display)
timer.start()

print("Main Thread")