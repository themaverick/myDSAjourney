def subStr(str1, s, el):
    if s >= len(str1):
        print(el)
        return
    
    subStr(str1, s+1, el)
    el = el + str1[s]
    subStr(str1, s+1, el)


string = "abc"

subStr(string, 0, '')
