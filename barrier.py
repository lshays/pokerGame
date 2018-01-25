from threading import Semaphore, Thread
import time

class Barrier:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.mutex = Semaphore(1)
        self.barrier = Semaphore(0)
        self.barrier2 = Semaphore(1)

    def wait(self):
        self.mutex.acquire()
        self.count += 1
        if self.count == self.n:
            self.barrier2.acquire()
            self.barrier.release()
        self.mutex.release()
        
        self.barrier.acquire()
        self.barrier.release()
        
        self.mutex.acquire()
        self.count -= 1
        if self.count == 0:
            self.barrier.acquire()
            self.barrier2.release()
        self.mutex.release()
        
        self.barrier2.acquire()
        self.barrier2.release()

b = Barrier(2)

def func1():
    while True:
        time.sleep(1)
        #
        b.wait()
        #
        print('Working from func1')

def func2():
    while True:
        time.sleep(0.5)
        #
        b.wait()
        #
        print('Working from func2')

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start() 
