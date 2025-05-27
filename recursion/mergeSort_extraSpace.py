def merge(arr1, s, e):
    mid = (s+e)//2

    arrL = arr1[s:mid+1]
    arrR = arr1[mid+1:e+1]
    
    i = 0
    j = 0
    while i < len(arrL) and j < len(arrR):
        if arrL[i] < arrR[j]:
            arr1[s+i+j] = arrL[i]
            i += 1
        else:
            arr1[s+i+j] = arrR[j]
            j += 1
    while i < len(arrL):
        arr1[s+i+j] = arrL[i]
        i += 1
    while j < len(arrR):
        arr1[s+i+j] = arrR[j]
        j += 1

    del arrL
    del arrR ## python garbage collector already does this
    return
    

def mergeSort(arr1, s, e):
    
    if s >= e:
        return
    mid = (s+e)//2

    mergeSort(arr1, s, mid)

    mergeSort(arr1, mid+1, e)

    merge(arr1, s, e)


arr1 = [6, 9, 5, 2, 12, 8, 16, 1]

mergeSort(arr1, 0, len(arr1)-1)
print(arr1)