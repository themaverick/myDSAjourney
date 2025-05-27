def inPlaceMerge(arr1, s, e):
    mid = (s+e)//2
    
    i = s
    j = mid+1

    while (i <= mid and j <= e):
        if arr1[i] > arr1[j]:
            tmp = arr1[j]
            k = j
            while k > i:
                arr1[k] = arr1[k-1]
                k -= 1
            arr1[i] = tmp
            mid+=1
        i += 1
        j += 1
    return
        

def mergeSort(arr1, s, e):
    
    if s >= e:
        return
    mid = (s+e)//2

    mergeSort(arr1, s, mid)

    mergeSort(arr1, mid+1, e)

    inPlaceMerge(arr1, s, e)


arr1 = [6, 9, 5, 2, 12, 8, 16, 1]

mergeSort(arr1, 0, len(arr1)-1)
print(arr1)