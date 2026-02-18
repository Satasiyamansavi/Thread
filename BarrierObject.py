import threading 
import time
def player(name):
    print(f"{name} is started")
    score=0
    for i in range(3):
        time.sleep(1)
        print(f"{name} is palying")

    print(f"{name} scored {score}")
    print("Sending winning amount to {name}")
Thread=[]
player_name=['Raj','Rohan','Priya']
for name in player_name:
    thread=threading.Thread(target=player,args=(name,))
    Thread.append(thread)
    thread.start()