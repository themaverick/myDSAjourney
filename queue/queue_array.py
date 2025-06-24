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
