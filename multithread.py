#The main purpose of multithreading is to provide simultaneous execution of two or more parts of a program to maximum utilize the CPU time. A multithreaded program contains two or more parts that can run concurrently. Each such part of a program called thread.
#Multithreading is defined as the ability of a processor to execute multiple threads concurrently.
# a thread is a sequence of such instructions within a program that can be executed independently of other code.

import threading 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
#     # wait until thread 1 is completely executed 
#     t1.join() 
#     # wait until thread 2 is completely executed 
#     t2.join() 
 
# print_square(10)
# print_cube(10)  
    # both threads completely executed 
    # print("Done!")