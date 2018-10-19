from threading import Thread
import time

def timer(name, delay, repeat):
    print('Timer: ' + name + ' Started')

    while repeat > 0:
        # tell the timer to wait for a certain amount of time
        time.sleep(delay)
        print(name + ": " + str(time.ctime(time.time())))

        # decrement the value - when the value is at 0 the function is complete
        repeat -= 1
    print("Timer: " + name + " Completed")

def Main():
    # creates 2 threads - the target is the 'timer' class which takes in the parameters name, delay, and how many times to repeat
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    
    # start the threads
    t1.start()
    t2.start()

    #print this out when it's complete
    print("Main Completed")

if __name__ == '__main__':
    Main()
    