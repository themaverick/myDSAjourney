def solution(array, idx, ans):
    if idx+1 >= len(array):
        return

    if array[idx] < 0:
        el = array[idx]
    elif array[idx+1] < 0:
        el = array[idx+1]
    else:
        el = 0
    
    ans.append(el)
    
    solution(array, idx+1, ans)

a = [-8, 3, -6, 2, 1, 6]
b = [-8, 2, 3, -6, 10]
sol = []

solution(b, 0, sol)

print(sol)
ans = [-8, -6, -6, 0, 0]