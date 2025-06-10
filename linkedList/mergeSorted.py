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

def mergeSorted(ll1, ll2):
    cur1 = ll1.head
    cur2 = ll2.head

    if cur1.data > cur2.data:
        ans = cur2
    else:
        ans = cur1

    while cur1 is not None and cur2 is not None:
        if cur1.data > cur2.data:
            if cur2.next is not None:
                if cur1.data < cur2.next.data:
                    fwd = cur2.next
                    cur2.next = cur1
                    cur2 = fwd
                elif cur1.data >= cur2.next.data:
                    cur2 = cur2.next
            else:
                cur2.next = cur1
                cur2 = None
        elif cur2.data >= cur1.data:
            if cur1.next is not None:
                if cur2.data < cur1.next.data:
                    fwd = cur1.next
                    cur1.next = cur2
                    cur1 = fwd
                elif cur2.data >= cur1.next.data:
                    cur1 = cur1.next
            else:
                cur1.next = cur2
                cur1 = None

    return ans

def mergeSortedPro(ll1, ll2):
    if ll1.head.data < ll2.head.data:
        ans = ll1.head
        cur1 = ll1.head.next
        cur2 = ll2.head
        current = ll1.head
    else:
        ans = ll2.head
        cur1 = ll2.head.next
        cur2 = ll1.head
        current = ll2.head

    while cur1 is not None and cur2 is not None:
        if cur1.data < cur2.data:
            current.next = cur1
            cur1 = cur1.next
        else:
            current.next = cur2
            cur2 = cur2.next
        current = current.next
    if cur1 is not None:
        current.next = cur1
    elif cur2 is not None:
        current.next = cur2
    
    return ans

a = LinkedList()
b = LinkedList()
a.insertAtTail(1)
a.insertAtTail(3)
a.insertAtTail(16)
a.insertAtTail(16)
a.insertAtTail(20)
b.insertAtTail(1)
b.insertAtTail(1)
b.insertAtTail(4)
b.insertAtTail(6)
b.insertAtTail(8)
b.insertAtTail(90)

a.printList()
b.printList()

sorted = mergeSortedPro(a, b)

printll(sorted)



