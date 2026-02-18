from threading import Thread,main_thread,active_count,get_native_id,enumerate
def display():
    print("Before id:",get_native_id())
    print("The Main Thread:",main_thread())
    print("Disply Method")
def show():
    print("Show Method")
t1=Thread(target=display)
t2=Thread(target=show)
print("Before:",t1.is_alive())
t1.start()
print("After id:",get_native_id())
print("Number of Thread",active_count())
print("Number of Enumeration",enumerate())
print("After:",t1.is_alive())