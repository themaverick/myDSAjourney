class nQueueArray:
    def __init__(self, n, size):
        self.n = n
        self.size = size
        self.queue = [-1]*size
        self.next = [i+1 for i in range(self.size)]
        self.next[-1] = -1
        self.front = [-1]*self.n
        self.rear = [-1]*self.n
        self.freespot = 0

    def push(self, element, n):
        if self.freespot == -1:
            print("queue overflow")
            return
        # print(f"self.freespot: {self.freespot}, self.next[self.freespot]: {self.next[self.freespot]}")
        index = self.freespot
        self.freespot = self.next[self.freespot]
        self.queue[index] = element
        self.next[index] = self.rear[n]
        self.rear[n] = index

        if self.front[n] == -1:    
            self.front[n] = index

        return
    
    def pop(self, n):
        if self.front == -1:
            print("Queue Underflow")
            return
        
        el_idx = self.front[n]
        el = self.queue[el_idx]
        for idx in range(len(self.next)):
            if self.next[idx] == self.front[n]:
                self.front[n] = idx
                self.next[idx] = -1
                break

        self.queue[el_idx] = -1
        self.next[el_idx] = self.freespot
        self.freespot = el_idx

        return el


class nQueueArray_v2:
    def __init__(self, n, size):
        self.n = n
        self.size = size
        self.queue = [-1]*size
        self.next = [i+1 for i in range(self.size)]
        self.next[-1] = -1
        self.front = [-1]*self.n
        self.rear = [-1]*self.n
        self.freespot = 0

    def push(self, element, n):
        if self.freespot == -1:
            print("queue overflow")
            return
        # print(f"self.freespot: {self.freespot}, self.next[self.freespot]: {self.next[self.freespot]}")
        index = self.freespot
        self.freespot = self.next[self.freespot]
        self.queue[index] = element

        if self.front[n] == -1:
            self.front[n] = index
            self.next[index] = -1
        else:
            self.next[self.rear[n]] = index
        self.rear[n] = index

        return
    
    def pop(self, n):
        if self.front[n] == -1:
            print("Queue Underflow")
            return
        
        el_idx = self.front[n]
        el = self.queue[el_idx]
        self.front[n] = self.next[el_idx]
        self.next[el_idx] = self.freespot
        self.freespot = el_idx
        self.queue[el_idx] = -1

        return el


nQ =  nQueueArray_v2(3, 7)

nQ.push(2, 0)
# print(f"queue: {nQ.queue}, next: {nQ.next}, front: {nQ.front}, rear: {nQ.rear}")
nQ.push(3, 0)
nQ.push(5, 0)
nQ.push(1, 1)
nQ.push(4, 1)
nQ.push(7, 0)
# print(f"queue: {nQ.queue}, next: {nQ.next}, front: {nQ.front}, rear: {nQ.rear}")
nQ.pop(0)
print(f"queue: {nQ.queue}, next: {nQ.next}, front: {nQ.front}, rear: {nQ.rear}")

