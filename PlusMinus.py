#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    for value in arr:
        if value > 0:
            positive += 1
        elif value < 0:
            negative += 1
        else:
            zero += 1
    n = len(arr)
    res = [positive / n, negative / n, zero / n]
    for i in range(len(res)):
        res[i] = round(res[i], 6)
    print(res)
    return res
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
