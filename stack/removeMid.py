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

def removeMid_w_stack(s):
    s2 = stack()

    mid = s.size()//2 + 1

    for i in range(mid):
        s2.push(s.pop())
    
    s2.pop()
    
    while not s2.is_empty():
        s.push(s2.pop())

    return

def removeMid(s, c, size):
    mid = size//2 + 1

    if c == mid:
        s.pop()
        return
    
    el = s.pop()

    removeMid(s, c+1, size)

    s.push(el)


s = stack()
s.push("a")
s.push("v")
s.push("e")
s.push("r")
s.push("a")
s.push("g")
s.push("e")
s.push("j")
s.push("o")
s.push("e")

removeMid(s, 1, s.size())
while not s.is_empty():
    print(s.pop())


