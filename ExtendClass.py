from threading import Thread
from time import sleep
movie=['Vivah','Hum Sath Sath Hain','Hum Apke Hain Kaun']
class demo(Thread):
    def __init__(self):
        print("Constructor call")
        Thread.__init__(self)
    def run(self):
        a=10
        b=20
        for i in movie:
            print(f"{i} Started Uploading")
            sleep(1)
            print(f"{i} Uploaded!")
        self.temp=a+b
        print("Sum:",self.temp)
d1=demo()
d1.start()
sleep(2)
for i in range(3):
    sleep(0.5)
    print("Checking Copyright")