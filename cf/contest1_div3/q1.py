import math

t = int(input())
for _ in range(t):
    s = input()
    num = int(s)
    root = math.isqrt(num)  # integer sqrt

    if root * root == num:
        print(0, root)
    else:
        print(-1)