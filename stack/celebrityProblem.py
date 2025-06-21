def knows(a, b):
    if M[a][b] == 1:
        return True
    return False

def getCelebrity(M, n):
    stk = []

    for i in range(n):
        stk.append(i)

    while len(stk) > 1:
        a = stk.pop()
        b = stk.pop()

        if knows(a, b):
            stk.append(b)
        else:
            stk.append(a)
    
    candidate = stk[0]

    if M[candidate] == [0]*n:
        n_cnt = 0
        for k in range(n):
            if M[k][candidate] == 1:
                n_cnt += 1
        if n_cnt == n-1:
            return candidate
    return -1


M = [[0, 1, 0],
     [0, 0, 0], 
     [1, 1, 0]]

print(getCelebrity(M, 3))