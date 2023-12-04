while True:
    arr = list(map(int, input("Enter 0s and 1s separated by space: ").split()))
    valid = True
    for i in range(len(arr)):
        if arr[i] not in [0, 1]:
            valid = False
            break
    if valid:
        break
