#!/usr/bin/env python

import os
import time

"""
Invoke a hello world program (java or any other language) and 
programmatically measure the time taken to execute the program
     Time measurement can be done in the program itself or in the invoker
     Time measurement should be in nano second precision
      Any hello world program can be used
"""

INVOKER = "./HelloWorld"


def calculate_time(system_call_cmd):
    start_time = time.time()
    os.system(system_call_cmd)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    calculate_time(INVOKER)
