class nStacks:
    def __init__(self, size_array, num_stacks):
        self.size = size_array
        self.num_stacks = num_stacks

        self.array = [-1] * self.size
        self.top = [-1] * self.num_stacks
        self.next = [i+1 for i in range(self.size)]
        self.next[-1] = -1

        self.freespot = 0

    def push(self, element, stack):
        index = self.freespot

        if index == -1:
            print("stack overflow")
            return False

        # insert element
        self.array[index] = element
        # update freespot
        self.freespot = self.next[index]
        # update next array
        self.next[index] = self.top[stack-1]
        # update the top array
        self.top[stack-1] = index

        return True
    
    def pop(self, stack):
        
        if self.top[stack-1] == -1:
            print("stack underflow.")
            return False
        
        index = self.top[stack-1]

        self.array[index] = -1

        self.top[stack-1] = self.next[index]

        self.next[index] = self.freespot

        self.freespot = index

        return True
    

s = nStacks(9, 3)

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in arr1:
    print(s.push(i, 1))
    print(f"array: {s.array}, next: {s.next}, top: {s.top}")

for i in range(len(arr1)):
    s.pop(1)
    print(f"array: {s.array}, next: {s.next}, top: {s.top}")
    