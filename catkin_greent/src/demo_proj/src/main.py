from threading import Thread
import os
from time import sleep

def t2():
    os.system("rosrun rosserial_python serial_node.py /dev/ttyACM0")

def t1():
    os.system("roslaunch demo_proj demo_proj.launch")

def t3():
    os.system("xboxdrv --silent")

def t4():
    os.system("rosrun joy joy_node")

if __name__ == "__main__":
    t1 = Thread(target=t1)
    t2 = Thread(target=t2)
    t3 = Thread(target=t3)
    t4 = Thread(target=t4)
    t = [t1,t2,t3,t4]
    for i in range(len(t)-1):
        t[i].start()
        sleep(1)
    for j in range(len(t)-1):
        t[j].join()
    print("exit")