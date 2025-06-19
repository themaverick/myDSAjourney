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


def insertSort(s, el):
    if s.is_empty() or s.peek() < el:
        s.push(el)
        return
    
    num = s.pop()
    insertSort(s, el)
    s.push(num)


def sort(s):
    if s.is_empty():
        return
    
    num = s.pop()
    sort(s)
    insertSort(s, num)



str1 = "12782"
s = stack()

for i in str1:
    s.push(int(i))

sort(s)

while not s.is_empty():
    print(s.pop())




