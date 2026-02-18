from threading import Thread,current_thread
def display(self):
    print("Disply Method")
def show(self):
    print("Show Method")
t1=Thread(target=display)
t2=Thread(target=show)
t1.setName("Dharmi")
print(t1.name)
print(t2.name)
current_thread().name='Mansvi'
print(current_thread().name)