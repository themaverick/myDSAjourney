def binSearch(arr, strIdx, endIdx, el):
    if strIdx > endIdx:
        return False
    
    midIdx = strIdx + int(endIdx/2 - strIdx/2)
    if el == arr[midIdx]:
        return True
    elif el < arr[midIdx]:
        return binSearch(arr, strIdx, midIdx-1, el)
    else:
        return binSearch(arr, midIdx+1, endIdx, el)
    
arr1 = [2, 4, 6, 9, 11, 13]

print(f"result: {binSearch(arr1, 0, len(arr1), 10)}")