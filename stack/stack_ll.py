class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, data):
        el = Node(data)
        if self.is_empty():
            self.head = el
        else:
            el.next = self.head
            self.head = el
        self.size += 1
        return
    
    def pop(self):
        if self.is_empty():
            raise ValueError('stack underflow')
        
        if self.size == 1:
            self.head = None
        else:
            fwd = self.head.next
            self.head.next = None
            self.head = fwd
        self.size -= 1
        return
    
    def is_empty(self):
        is_emp = True if not self.size else False
        return is_emp

    def peek(self):
        if self.is_empty():
            raise ValueError('stack is empty.')
        return self.head.data


s = stack()
s.push(1)
s.push(5)
s.push(3)
s.push(4)
print(s.peek())
s.pop()
s.pop()
print(s.size)

print(s.peek())
s.pop()
s.pop()
# s.pop()

print(s.size)
print(s.peek())