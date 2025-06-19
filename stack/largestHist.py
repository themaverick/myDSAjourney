def nextSmall(arr1, n):
    ans = [-1] * n
    stk = []

    for i in range(n-1, -1, -1):
        while stk and arr1[stk[-1]] > arr1[i]:
            stk.pop()
        if stk:
            ans[i] = stk[-1]
        stk.append(i)
    return ans

def prevSmall(arr1, n):
    ans = [-1] * n
    stk = []

    for i in range(n):
        while stk and arr1[stk[-1]] > arr1[i]:
            stk.pop()
        if stk:
            ans[i] = stk[-1]
        stk.append(i)
    return ans

def largestHist(arr1, n):
    prev = prevSmall(arr1, n)
    next = nextSmall(arr1, n)

    area = 0
    for i in range(n):
        if next[i] == -1:
            next[i] = n
        l = arr1[i]
        b = next[i] - prev[i] - 1
        if area < l*b:
            area = l*b

    return area
arr1 = [4, 5, 2, 10, 8]
# arr1 = [2, 1, 5, 6, 2, 3]

print(largestHist(arr1, len(arr1)))