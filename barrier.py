from threading import Semaphore, Thread
import time

class Barrier:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.mutex = Semaphore(1)
        self.barrier = Semaphore(0)
        # Untested waiting variable
        self.n_waiting = 0

    def wait(self):
        self.mutex.acquire()
        self.count = self.count + 1
        self.n_waiting += 1
        self.mutex.release()
        if self.count == self.n: self.barrier.release()
        self.barrier.acquire()
        self.barrier.release()
        # Untested waiting method below
        self.mutex.acquire()
        self.n_waiting -= 1
        self.mutex.release()
        
    # Waits until all threads have crossed barrier, then resets
    def reset(self):
        while self.n_waiting != 0:
            pass
        self.__init__(self.n)
        
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
