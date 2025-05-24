def isSorted(arr, idx):
    if idx >= len(arr)-1:
        return True
    if arr[idx] <= arr[idx+1]:
        return isSorted(arr, idx+1)
    else:
        return False
    
arr1 = [2, 4, 6, 9, 11, 13]

print(f"result: {isSorted(arr1, 0)}")