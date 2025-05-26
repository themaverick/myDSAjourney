def rev(s, idx, mid):
    if idx >= mid:
        return s
    el = s[idx]
    s[idx] = s[(-1-idx)]
    s[(-1-idx)] = el
    rev(s, idx+1, mid)

class Solution:
            
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s)%2 == 1:
            mid = (len(s)-1)/2 
        else:
            mid = len(s)/2
        
        return rev(s, 0, mid)
        

        