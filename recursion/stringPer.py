def stringPer(el, idx, res):
    if idx >= len(el):
        res.append("".join(el))
        return
    
    for i in range(idx, len(el)):
        el[idx], el[i] = el[i], el[idx]
        stringPer(el, idx+1, res)
        el[idx], el[i] = el[i], el[idx] 
str1 = list("abc")
res = []

stringPer(str1, 0, res)
print(res)
