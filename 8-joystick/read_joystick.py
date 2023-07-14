''' 
format of the /dev/input/js0 file: 8 bytes
unsigned integer (4 bytes) : time
signed short integer (2 bytes) : value, axis position, 0 for center, 1 for buttonpress, 0 for button release
signed characters (1 byte) : event type 1 for buttons, 2 for axis
signed characters (1 byte) : index, button/axis number (0 for x-axis)
'''

#!/usr/bin/python2
import struct
import threading
import time

joy = [0,0,0,0]

class readThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        # threadLock.acquire()
        print ("Start reading: " + self.name)
        readJoystick()
        print ("End reading: " + self.name)
        # threadLock.release()
        
#read joystick thread
def readJoystick():
    count = 3
    with open("/dev/input/js0", "rb") as f:
        while count:
            time.sleep(1)
            a = f.read(8)
            global joy 
            joy = list(struct.unpack("<Ihbb", a))
            print("t: {:10d} ms, value: {:6d}, code: {:1d}, index: {:1d}".format(joy[0], joy[1], joy[2], joy[3]))
            count -= 1

class printThread (threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        # threadLock.acquire()
        print ("Start printing: " + self.name)
        printJoystick()
        print ("End printing: " + self.name)
        # threadLock.release()

#read joystick thread
def printJoystick():
    count = 1
    while count:
        time.sleep(1)
        print("t: {:10d} ms, value: {:6d}, code: {:1d}, index: {:1d}".format(joy[0], joy[1], joy[2], joy[3]))
        count -= 1


# Start the main thread
if __name__ == "__main__":
    threadLock = threading.Lock()
    threads = []

    thread1 = readThread(1, "Thread-read", 1)
    thread2 = printThread(2, "Thread-print", 2)

    thread1.start()
    thread2.start()

    # thread1.join()
    # thread2.join()

    # while True:

    print ("退出主线程")
    # main()
    # readJoystick()