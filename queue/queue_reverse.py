import copy

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

    def reverse_queue(self):
        if self.is_empty():
            print('queue is empty')
            return -1
        elif len(self.queue) == 1:
            return
        
        i = 0
        while i < len(self.queue)//2:
            self.queue[i], self.queue[len(self.queue)-i-1] = self.queue[len(self.queue)-i-1], self.queue[i]
            i += 1
        return


a = [1, 2, 3, 4, 5]
q = queue()

for i in a:
    q.push(i)

p = copy.deepcopy(q)

while not p.is_empty():
    print(p.pop())

q.reverse_queue()
print('reversing queue.')

while not q.is_empty():
    print(q.pop())