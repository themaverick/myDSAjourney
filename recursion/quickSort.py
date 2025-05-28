def partition(arr1, s, e):
    p = s

    for i in arr1[s:e+1]:
        if i < arr1[s]:
            p += 1
    arr1[p], arr1[s] = arr1[s], arr1[p]

    j = s
    k = e
    while j < p and k > p:
        if arr1[j] >= arr1[p]:
            if arr1[k] < arr1[p]:
                arr1[j], arr1[k] = arr1[k], arr1[j]
                j += 1
                k -=1
            else:
                k-=1
        elif arr1[k] < arr1[p]:
            j += 1
        else:
            j+=1
            k-=1

    # while j < p and k > p:
    #     while(arr1[j] < arr1[p]):
    #         j += 1
    #     while(arr1[k] >= arr1[p]):
    #         k -=1
        
    #     if j < p and k > p:
    #         arr1[j], arr1[k] = arr1[k], arr1[j]
    #         j += 1
    #         k -= 1

    return p

def quickSort(arr1, s, e):
    if s >= e:
        return 

    p = partition(arr1, s, e)

    quickSort(arr1, s, p-1)
    quickSort(arr1, p+1, e)

arr1 = [2, 32, 1, 4, 6, 2, 54, 22, 6, 2]

quickSort(arr1, 0, len(arr1) - 1)

print(arr1)

## make sure to handle equal element (either on left of pivot or on right)