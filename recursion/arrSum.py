def arrSum(arr, idx, sum):
    if idx >= len(arr):
        return sum
    return arrSum(arr, idx+1, sum+arr[idx])
    
arr1 = [2, 4, 6, 9, 11, 13]

print(f"result: {arrSum(arr1, 0, 0)}")