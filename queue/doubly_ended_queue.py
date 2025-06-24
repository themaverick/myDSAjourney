class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.insert(0, element)
        return element
    
    def dequeue(self):
        if self.is_empty():
            print('queue underflow')
            return
        return self.queue.pop(0)
    
    def enqueue_back(self, element):
        self.queue.append(element)
        return element
    
    def dequeue_back(self):
        if self.is_empty():
            print('queue underflow')
            return
        return self.queue.pop(-1)     

    def is_empty(self):
        return not self.queue