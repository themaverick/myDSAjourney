def checkPalindrome(str1, idx, mid):
    if idx >= mid:
        return True
    if str1[idx] != str1[-1-idx]:
        return False
    return checkPalindrome(str1, idx+1, mid)

str1 = "hebhibeh"
if len(str1)%2 == 1:
    mid = (len(str1)-1)/2 
else:
    mid = len(str1)/2

print(checkPalindrome(str1, 0, mid))