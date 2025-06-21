def nextSmall(arr1, n):
    ans = [-1] * n
    stk = []

    for i in range(n-1, -1, -1):
        while stk and arr1[stk[-1]] >= arr1[i]:
            stk.pop()
        if stk:
            ans[i] = stk[-1]
        stk.append(i)
    return ans

def prevSmall(arr1, n):
    ans = [-1] * n
    stk = []

    for i in range(n):
        while stk and arr1[stk[-1]] >= arr1[i]:
            stk.pop()
        if stk:
            ans[i] = stk[-1]
        stk.append(i)
    return ans

def largestArea(arr1, n):
    prev = prevSmall(arr1, n)
    next = nextSmall(arr1, n)
    print(f"prevSmall: {prev}, nextSmall: {next}")

    area = 0
    for i in range(n):
        if next[i] == -1:
            next[i] = n
        l = arr1[i]
        b = next[i] - prev[i] - 1
        if area < l*b:
            area = l*b

    return area

def maxRectangle(arr, n, m):

    area = largestArea(arr[0], m)
    print(f"maximum area for 0 row as base: {area}")
    for i in range(1, n):
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] += arr[i-1][j]
            else:
                arr[i][j] = 0
        area = max(area, largestArea(arr[i], m))
        print(f"maximum area for {i} row as base: {area}")
    
    return area


areas = [[0, 1, 1, 1],
         [1, 1, 1, 1], 
         [1, 1, 1, 1],
         [1, 1, 1, 0]]

print(maxRectangle(areas, 4, 4))