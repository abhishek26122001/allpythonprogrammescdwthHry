from threading import Thread, current_thread
import os

def thread1():
    print("Thread 1 name: ", current_thread().name)
    print("Thread 1 ID : ", os.getpid())
                                                       #function creation
def thread2():
    print("Thrad 2 name: ", current_thread().name)
    print("Thread 2 ID : ", os.getpid())    


if __name__ == "__main__":

    print("Main Program Thread Name: ", current_thread().name)
    print("Main Program ID is ", os.getpid())


    t1 = Thread(target=thread1, name="t1")
    t2 = Thread(target=thread2, name= "t2")                               # Thread Creation




    t1.start()
    t2.start()                   # Strating the thread


    t1.join()
    t2.join()                       # Wait till the threads are completed

    print("Thread Process Completed")    
    