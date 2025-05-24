def linSearch(arr, idx, el):
    if idx >= len(arr):
        return False
    if arr[idx] == el:
        return True
    return linSearch(arr, idx+1, el)
    
arr1 = [2, 4, 6, 9, 11, 13]

print(f"result: {linSearch(arr1, 0, 13)}")
print(arr1)