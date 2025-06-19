class stack:
    def __init__(self):
        self.top = -1
        self.arr = []

    def push(self, data):
        self.arr.append(data)
        self.top += 1
        return
    
    def pop(self):
        if self.is_empty():
            raise ValueError('stack underflow')

        self.top -= 1
        
        return self.arr.pop()
    
    def size(self):
        return self.top + 1
    
    def is_empty(self):
        is_emp = True if self.top == -1 else False
        return is_emp

    def peek(self):
        if self.is_empty():
            raise ValueError('stack is empty.')
        return self.arr[self.top]

def balancedBrac(str1):
    bracDict = {
        "{": "}",
        "[": "]",
        "(": ")"
    }

    s = stack()
    for i in str1:
        if i in bracDict.keys():
            s.push(i)
        elif i == bracDict[s.peek()]:
            s.pop()
        else:
            return -1

    if s.is_empty():
        return 0
    return -1
            


str1 = "{[([])]}["

print(balancedBrac(str1))


