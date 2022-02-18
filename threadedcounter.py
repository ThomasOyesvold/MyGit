# Create a script threadedcounter.py.
# In this script you are required to manually create 2 threads.
# The one thread should start on a function called incrementor and the other should start on a function called decrementor.
# Both the functions should receive a numeric value as an argument.
# The two threads should both receive the same numeric argument.
# Use logging to display how the one function increments the value and the other decrements the value.
# The main program should wait until both threads have finished their execution before ending the program.
import threading
import logging
import concurrent.futures
import time

class threadedcounter():
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def incrementor(self,name):
        logging.info("Incrementor: Starting incrementing.".format(name))
        with self._lock:
            local_value = self.value
            local_value += 1
            time.sleep(0.1)
            self.value = local_value
            logging.info("Value now updated to {}".format(self.value))

    def decrementor(self,name):
        logging.info("Decrementor: Is decrementing.".format(name))
        with self._lock:
            local_value = self.value
            local_value -= 1
            time.sleep(0.1)
            self.value = local_value
            logging.info("Value now updated to {}".format(self.value))

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,datefmt="%H:%M:%S")
logging.getLogger().setLevel(logging.DEBUG)

number = threadedcounter()
logging.info("The value is currently {}".format(number.value))
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    for index in range(4):
        executor.submit(number.incrementor, index)
    for index in range(3):
        executor.submit(number.decrementor,index)
logging.info("The value is updated. Ending value is {}".format(number.value))