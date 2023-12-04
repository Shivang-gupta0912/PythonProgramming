import array

arr3 = array.array( 'i',[3,5,67,8,9])
arr4 = array.array('i', [])
print(arr3)
print(arr4)

import numpy

arr=numpy.array([1,6,3,8])
arr2 = numpy.array( [1,23,45,6,9],dtype=int) #keyword arg does not follow positional arg

print(arr)
print(arr2)