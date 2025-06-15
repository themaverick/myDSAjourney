class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

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
            temp.random = temp
            return
        self.tail.next = temp
        self.tail = temp
        self.tail.random = self.head
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
            print(f"({temp.data}, {temp.random.data})", end=" -> " if temp.next else "")
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

def cloneLL(a):
    cur = a.head
    clone = LinkedList()
    old_to_new = {}
    while cur is not None:
        clone.insertAtTail(cur.data)
        old_to_new[cur] = clone.tail
        cur = cur.next
    
    cur1 = a.head
    while cur1 is not None:
        old_to_new[cur1].random = old_to_new[cur1.random]

        cur1 = cur1.next
        
    return clone

a = LinkedList()
a.insertAtTail(3)
a.insertAtTail(4)
a.insertAtTail(5)
a.insertAtTail(4)
a.insertAtTail(5)

a.printList()
b = cloneLL(a)

b.printList()



