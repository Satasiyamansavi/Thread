from threading import *
from time import sleep
l1=RLock()
class Student:
    def __init__(self,name,available_seats,l):
        self.available_seats=available_seats
        self.name=name
        self.l=l
    def register(self,need_seats):
        self.l.acquire()
        self.l.acquire()
        print(self.l)
        print("Availabl seats are:",self.available_seats)
        if(self.available_seats>=need_seats):
            nm=current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print("Seats are not available")
        self.l.release()
        self.l.release()
s1=Student("Parvati",4,l1)
t1=Thread(target=s1.register,args=(1,),name="Mansvi")
t2=Thread(target=s1.register,args=(2,),name="Dharmi")
t1.start()
t2.start()