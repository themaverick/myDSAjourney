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


def minimumCost(str1):
    if len(str1) % 2 == 1:
        return -1
    
    stk = stack()
    for i in str1:
        if i == "{":
            stk.push(i)
        else:
            if not stk.is_empty() and stk.peek() == "{":
                stk.pop()
            else:
                stk.push(i)
    
    a = 0
    b = 0
    while not stk.is_empty():
        el = stk.pop()
        if el == "{":
            a += 1
        else:
            b += 1
    
    return (a+1)//2 + (b+1)//2
 


str1 = r"{{}}}}"

print(minimumCost(str1))





