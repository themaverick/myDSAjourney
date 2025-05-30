def phoneNumber(str1, idx, el, result):
    if idx >= len(str1):
        result.append(el)
        return
    
    for i in phDict[str1[idx]]:
        el = el + i
        phoneNumber(str1, idx+1, el, result)
        el = el[:-1]

phDict = {
    '2': ['a', 'b', 'c'], 
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

str1 = '23'
el = ''
result = []
phoneNumber(str1, 0, el, result)
print(result)