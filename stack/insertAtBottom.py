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

def insertAtBottom(stack, el):

    if stack.is_empty():
        stack.push(el)
        return

    num = stack.pop()
    insertAtBottom(stack, el)
    stack.push(num)

    return
            


str1 = "2321"
s = stack()

for i in str1:
    s.push(int(i))

insertAtBottom(s, 1)

while not s.is_empty():
    print(s.pop())



