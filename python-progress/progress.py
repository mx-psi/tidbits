#!/usr/bin/python3
# Author: Pablo Baeyens

import threading
import time

class progress:
  """Manage waiting messages on Python.

  >>> with progress("message"):
  ...   do_something()

  will print a progress `message` while `do_something` finishes.
  The progress printing thread is terminated even when
  exceptions are raised.

  `something` must NOT print anything, otherwise the output will be garbled.

  Inspired by stackoverflow.com/a/39504463/3414720
  """

  def __init__(self, msg):
    self.msg = "> " + msg + ": "
    self.running = False
    self.delay = 0.3

  def wait(self):
    """Function of thread that prints progress."""
    i = 0
    wait = ["   ", ".  ", ".. ", "..."]
    while self.running:
      print(self.msg + wait[i], end="\r", flush=True)
      time.sleep(self.delay)
      i = (i+1) % 4

  def __enter__(self):
    """Starts thread."""
    self.running = True
    threading.Thread(target=self.wait).start()

  def __exit__(self, exception, value, tb):
    """Stops thread and prints end message."""
    self.running = False
    if exception is not None:
      print()
      return False
    print(self.msg + "done.")



if __name__ == "__main__":
  # Usage example
  with progress("Adding up all numbers from 1 to 10⁸"):
    total = 0
    for i in range(10**8):
      total += i

  print("Total sum: {}".format(total))
