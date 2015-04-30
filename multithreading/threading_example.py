__author__ = 'alexmcneill'


import threading
import time

def timer(name, delay, repeat):
    print("Timer" + name + " starting")
    for i in xrange(repeat):
        time.sleep(delay)
        print(name+" "+time.ctime(time.time()))
    print("Timer " + name + "  finishing. ")

if __name__ == "__main__":
    t1 = threading.Thread(target=timer, args=("timer 1", 2, 5))
    t2 = threading.Thread(target=timer, args=("timer 2", 4, 5))
    t1.start()
    t2.start()

    print("Main Complete")