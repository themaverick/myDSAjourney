def isPoss(str1, n, k):
    if k > n//2:
        print("NO")
        return
    cntDict = {
        "0": 0, 
        "1": 0
    }
    for i in str1:
        cntDict[i] += 1
    
    pairs = 0
    for i in cntDict.values():
        pairs += i//2
    if pairs < k:
        print("NO")
        return
    print("YES")
    return

num = int(input())
for _ in range(num):
    n, k = map(int, input().split())
    str1 = input().strip()
    isPoss(str1, n, k)