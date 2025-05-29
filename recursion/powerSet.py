def powerSet(arr1, el, s, result):
    if s >= len(arr1):
        result.append(el[:])
        return 
    
    powerSet(arr1, el, s+1, result)
    el.append(arr1[s])
    powerSet(arr1, el, s+1, result)
    el.pop()

arr1 = ["a", "b", "c", "d"]
result = []
# el = []
powerSet(arr1, [], 0, result)
print(result)
