from array import *

arr=array('d', [4.3,5.7,8.9,3.5])

def traverse(array):
    for ele in array:
        print(ele)

traverse(arr)

# time complexity = o(n)
# to print n elements using for loop

# space complexity = o(1)
# bcz we don't have to provide an extra space for traveresing the elements