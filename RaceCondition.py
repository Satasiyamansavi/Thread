from threading import *
from time import sleep

class Student:
    def __init__(self,name,available_seats,):
        self.available_seats=available_seats
        self.name=name
    def register(self,need_seats):
        print("Availabl seats are:",self.available_seats)
        if(self.available_seats>=need_seats):
            nm=current_thread().name
            print(f"{need_seats} are allocated to {nm}")
            self.available_seats-=need_seats
        else:
            print("Seats are not available")
s1=Student("Parvati",4)
t1=Thread(target=s1.register,args=(1,),name="Mansvi")
t2=Thread(target=s1.register,args=(2,),name="Dharmi")
t1.start()
t2.start()