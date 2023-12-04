import array

def linearSearch(arr, value:int):
    found = 0
    for i in range(len(arr)):
        if arr[i] == value:
            found=1
            print(f"{value} found at location {i}")
    if found==0:
        print("Value not found...")   


arr = array.array('i', [4,5,6,8,2,9,1,7,2,3,5])
linearSearch(arr,2)


# time complexity -> O(n)
# space complexity -> O(1)

# Note 
# time complexity of len() function -> O(1) because it stores len value of array
# also, time complexity of range() function -> O(1) as it not generate the sequence rather it creates a iterator which generates no.(s) on demand
