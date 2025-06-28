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

def firstNonrepeatingChar(arr1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    dict1 = {alp: 0 for alp in alphabet}
    res = []

    for i in arr1:
        dict1[i] += 1
        if dict1[i] == 1:
            res.append(i)
        elif dict1[i] == 2:
            for idx, j in enumerate(res):
                if j == i:
                    res.pop(idx)
                    break
        
        if res:
            # print(f'res list: {res}, dict1: {dict1}')
            print(res[0])
        else:
            print('#')
    return


array = ['a', 'b', 'c', 'a', 'c', 'b']

firstNonrepeatingChar(array)