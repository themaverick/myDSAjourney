import copy

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

class queue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)
        return element
    
    def pop(self):
        if self.is_empty():
            print('queue underflow')
            return

        return self.queue.pop(0)

    def is_empty(self):
        return not self.queue

    def size(self):
        return len(self.queue)
    
    def front(self):
        if self.is_empty():
            print('queue is empty')
            return
        return self.queue[0]
    
    def rear(self):
        if self.is_empty():
            print('queue is empty')
            return
        return self.queue[-1]

def reverse_firstk(q, k):
    stk = stack()

    for i in range(k):
        el = q.pop()
        stk.push(el)

    while not stk.is_empty():
        el = stk.pop()
        q.push(el)

    for j in range(len(q.queue) - k):
        el = q.pop()
        q.push(el)

    return



arr = [1, 2, 3, 4, 5, 6]
que = queue()

for i in arr:
    que.push(i)

que2 = copy.deepcopy(que)

while not que.is_empty():
    print(que.pop())

reverse_firstk(que2, 3)
print('operation done.')

while not que2.is_empty():
    print(que2.pop())

