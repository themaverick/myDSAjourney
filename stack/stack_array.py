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

        self.arr.pop()
        self.top -= 1
        return
    
    def size(self):
        return self.top + 1
    
    def is_empty(self):
        is_emp = True if self.top == -1 else False
        return is_emp

    def peek(self):
        if self.is_empty():
            raise ValueError('stack is empty.')
        return self.arr[self.top]


s = stack()
s.push(1)
s.push(5)
s.push(3)
s.push(4)
print(s.arr)
print(s.top)
print(s.peek())
s.pop()
s.pop()

print(s.arr)
print(s.top)
print(s.peek())
s.pop()
s.pop()
# s.pop()

print(s.arr)
print(s.size())
print(s.top)
# print(s.peek())