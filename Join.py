from threading import Thread
from time import sleep

def upload():
    print("Start uploading movie...")
    sleep(3)
    print("Movie uploaded Successfully!")
def show():
    sleep(3)
    print("Send Notification to user for upload movie")
t1=Thread(target=upload)
t2=Thread(target=show)
t1.start()
t1.join()
t2.start()
t2.join()
for i in range(3):
    print("Welcome in movie set")