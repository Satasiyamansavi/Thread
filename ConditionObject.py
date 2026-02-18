import threading
import time
def write_data():
    con.acquire()
    with open("report.txt","w") as f1:
        days=["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"]
        for day in days:
            temp=input(f"Enter the temperature for {day}:")
            f1.write(temp+"\n")
    con.notify_all()
    con.release()
def max_data():
    con.acquire()
    con.wait(timeout=0)
    with open("report.txt","r") as f1:
        data=f1.readlines()
        max1=float(data[0].strip("\n"))
        for temp in data[1:]:
            temp=float(temp.strip("\n"))
            if temp>max1:
                max1=temp
        print("Maximum temperature is:",max1)
    con.release()
def avg_data():
    con.acquire()
    con.wait(timeout=0)
    with open("report.txt","r") as f1:
        data=f1.readlines()
        sum1=0
        for temp in data:
            temp=float(temp.strip("\n"))
            sum1=sum1+temp
        avg=sum1/len(data)
        print("Average temperature of week:",avg)
        con.release()
con=threading.Condition()
t1=threading.Thread(target=write_data)
t2=threading.Thread(target=max_data)
t3=threading.Thread(target=avg_data)
t1.run()
t2.run()
t3.run()