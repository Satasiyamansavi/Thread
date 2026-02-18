from threading import Thread
class demo:
    def display(self,n):
        for i in range(3):
            print("LOVE")
d1=demo()
t1=Thread(target=d1.display,args=(3,))
t1.start()
for i in range(2):
    print("YOU!")