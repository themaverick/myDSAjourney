def bubbleSort(arr1, end):
    if end == 0:
        return arr1

    for idx in range(end):
        if arr1[idx] > arr1[idx+1]:
            arr1[idx], arr1[idx + 1] = arr1[idx + 1], arr1[idx]
    return bubbleSort(arr1, end-1)

arr1 = [1, 23, 21, 45, 75, 2, 5, 64, 22, 5]

print(f"sorted array: {bubbleSort(arr1, len(arr1)-1)}")