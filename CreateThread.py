from threading import Thread, current_thread
def display(n,msg):
    print(current_thread().ident)
    for i in range(n):
        print(msg)

t1=Thread(target=display,kwargs={'n':2,'msg':"Vivah Movie"})
t1.start()

for i in range(2):
    print("Excelent!")