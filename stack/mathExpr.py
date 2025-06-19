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


def mathExpr(str1):
    stk = stack()

    for i in str1:
        if i in ["(", "+", "-", "*", "/"]:
            stk.push(i)
    
        elif i == ")":
            isRed = True
            while stk.peek() != "(":
                el = stk.pop()
                if el in ["+", "-", "/", "*"]:
                    isRed = False
            stk.pop()
    return isRed    



str1 = "(a+b)/(c*)"

print(mathExpr(str1))





