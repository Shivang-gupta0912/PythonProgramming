import array

arr = array.array('i', [4,56,89,76,15])

def accessElement(arr, index):
    if index<=len(arr) and index>=0 and type(index)==int:
        return arr[index]
    else:
        return "Wrong Index"

print(accessElement(arr, 2.5))

# time and space complexity for this code is o(1)