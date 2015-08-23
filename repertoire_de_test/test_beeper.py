import sys

import threading

def printit():
  threading.Timer(1.0, printit).start()
  sys.stdout.write('\a')
  sys.stdout.flush()


printit()
