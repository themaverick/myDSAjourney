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

def reverse(a):
    cur = a
    prev = None
    while cur is not None:
        fwd = cur.next
        cur.next = prev
        prev = cur
        cur = fwd
    return prev

def checkPalindrome(a):
    fast = a.head.next
    slow = a.head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    mid = slow
    temp = mid.next
    mid.next = reverse(temp)
    
    head1 = a.head
    head2 = mid.next
    while head2.next is not None:
        if head1.data != head2.data:
            mid.next = reverse(mid.next)
            return False
        else:
            head1 = head1.next
            head2 = head2.next
    mid.next = reverse(mid.next)
    return True    

a = LinkedList()
b = LinkedList()
a.insertAtTail(1)
a.insertAtTail(3)
a.insertAtTail(5)
a.insertAtTail(3)
a.insertAtTail(1)

a.printList()

print(checkPalindrome(a))
a.printList()



