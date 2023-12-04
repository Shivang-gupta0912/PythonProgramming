import array

arr = array.array('i', [3,5,7,8,4])
print(arr)
arr.insert(3, 67)
print(arr) 

#time complexity = o(n)
# bcz in worst case, we have to shift all elements to the right side for making the space for the newly element

#space complexity = o(1)
# bcz at the time of inserting , we have to make a space for only one element

