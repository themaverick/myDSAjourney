class Node:
    def __init__(self, element):
        self.data = element
        self.next = None


class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, element):
        el = Node(element)
        el.next = self.rear
        self.rear = el
        self.size += 1

        if self.size == 1:
            self.front = self.rear
        return element
    
    def dequeue(self):
        if self.is_empty():
            print('queue underflow')
            return

        if self.front == self.rear:
            el = self.front.data
            self.front = self.rear = None
            self.size -= 1
            return el

        cur = self.rear
        while cur.next != self.front:
            cur = cur.next
        self.front = cur
        el = cur.next.data
        cur.next = None
        self.size -= 1
        return el

    def is_empty(self):
        return self.size == 0
    
