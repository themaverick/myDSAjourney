def firstSmaller(arr1):
    ans = [-1 for i in arr1]

    stk = []

    for i in range(len(arr1)-1, -1, -1):
        while stk and arr1[stk[-1]] > arr1[i]:
            stk.pop()
        if stk:
            ans[i] = arr1[stk[-1]]
        stk.append(i)

    return ans


arr1 = [4, 5, 2, 10, 8]

ans = firstSmaller(arr1)
print(ans)