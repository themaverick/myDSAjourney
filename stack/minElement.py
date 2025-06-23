import numpy as np

class stk:
    def __init__(self, size):
        self.size = size
        self.array = [-1] * self.size
        self.top = -1
        self.mini = np.inf

    def push(self, element):
        if self.top >= self.size-1:
            print('stack overflow')
            return
        
        if  self.top == -1:
            add_el = element
            self.mini = add_el

        if self.mini <= element:
            add_el = element
        else:
            add_el =  2*element - self.mini
            self.mini = element

        self.array[self.top+1] = add_el
        self.top += 1
        return add_el


    def pop(self):
        if self.top == -1:
            print('stack underflow')
            return

        element = self.array[self.top]

        if element < self.mini:
            self.mini = 2*self.mini - element

        self.array[self.top] = -1
        self.top -= 1

        if self.top == -1:
            self.mini = np.inf

        return element


arr1 = [5, 2, 8, 3, 1]

stk1 = stk(7)

for i in arr1:
    print(stk1.push(i))
print(20*"--")
for i in range(len(arr1)):
    print(stk1.mini)
    stk1.pop()