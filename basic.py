from os import *
from sys import *
from collections import *
from math import *

from typing import List


def consecutiveOnes(arr: List[int]) -> int:
    highest_count=0
    for i in range (len(arr)):
        count=0
        
        while i<len(arr) and arr[i]==1:
            count+=1
            i+=1
        highest_count=max(count, highest_count)
        i+=1
    print(highest_count)


while True:
    arr = list(map(int, input().split()))
    valid = True
    for i in range(len(arr)):
        if arr[i] not in [0, 1]:
            valid = False
            break
    if valid:
        break

consecutiveOnes(arr)
