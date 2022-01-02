from threading import Thread

def  square(n):
    print("Square is: ", n*n)

def  cube(n):
    print("Cube is: ", n**3)

if __name__ == "__main__" :                        # using main in block concept


   # Thread creation
    n = int(input("Enter a number: "))
    st = Thread(target=square, args=(n,))
    ct = Thread(target=cube, args=(n, ))

    # Starting of Thread
    st.start()
    ct.start()


    #Wait till threads are completed

    st.join()
    ct.join()

    print("Thread Process Completed")
