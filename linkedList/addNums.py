class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtHead(self, data):
        temp = Node(data)
        temp.next =self.head
        self.head = temp
        if self.tail is None:
            self.tail = temp
        return

    def insertAtTail(self, data):
        temp = Node(data)

        if self.head is None:
            self.head = temp
            self.tail = temp
            return
        self.tail.next = temp
        self.tail = temp
        return

    def insertAtPos(self, data, pos):
        if pos < 1:
            raise ValueError("Position must be >= 1")
        
        if pos == 1:
            self.insertAtHead(data)
            return
        temp = Node(data)
        temp2 = self.head
        if pos >= 2:
            for i in range(pos-2):
                temp2 = temp2.next
                if temp2 is None:
                    raise IndexError("Out of bounds.")
        
        temp.next = temp2.next
        temp2.next = temp
        if temp.next is None:
            self.tail = temp
        return

    def deletePos(self, pos):
        if pos < 1:
            raise ValueError("Position must be >= 1.")
        
        if self.head is None:
            raise IndexError("Can't delete from an empty list.")

        if pos == 1:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        
        temp = self.head
        for i in range(pos-2):
            temp = temp.next
            if temp is None:
                raise IndexError("Out of bounds.")
        
        if temp.next is None:
            return
        elif temp.next.next is None:
            self.tail = temp
        temp.next = temp.next.next
        return

    def printList(self):
        temp = self.head
        while(temp != None):
            print(f"{temp.data}", end=" -> " if temp.next else "")
            temp = temp.next
        if temp is None:
            print()
        return

def printll(head):
    temp = head
    while(temp != None):
        print(f"{temp.data}", end=" -> " if temp.next else "")
        temp = temp.next
    if temp is None:
        print()
    return

def reverse(a):
    cur = a
    prev = None
    while cur is not None:
        fwd = cur.next
        cur.next = prev
        prev = cur
        cur = fwd
    return prev

def addNums(a, b):
    h1 = reverse(a.head)
    h2 = reverse(b.head)
    ans = LinkedList()

    cur1 = h1
    cur2 = h2

    carry = 0
    while cur1 is not None or cur2 is not None or carry!=0:
        if cur1 is None:
            d1 = 0
        else:
            d1 = cur1.data
        if cur2 is None:
            d2 = 0
        else:
            d2 = cur2.data
        elSum = d1 + d2 + carry
        carry = elSum//10
        el = elSum%10
        ans.insertAtHead(el)

        if cur1 is not None:
            cur1 = cur1.next
        if cur2 is not None:
            cur2 = cur2.next

    reverse(h1)
    reverse(h2)
    return ans

        

a = LinkedList()
b = LinkedList()
a.insertAtTail(3)
a.insertAtTail(4)
a.insertAtTail(5)

b.insertAtTail(4)
b.insertAtTail(5)

a.printList()
b.printList()

addNums(a, b).printList()
a.printList()
b.printList()




