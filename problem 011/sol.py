#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    # Define the date format
    date_format = '%a %d %b %Y %H:%M:%S %z'
    
    # Parse the dates using datetime.strptime which can handle the %z directive for timezone offsets
    dt1 = datetime.strptime(t1, date_format)
    dt2 = datetime.strptime(t2, date_format)
    
    # Calculate the difference in seconds
    time_difference = abs((dt1 - dt2).total_seconds())
    
    return str(int(time_difference))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')

    fptr.close()
