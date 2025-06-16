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


def mergeSorted(h1, h2):
    if h1 is None and h2 is None:
        return None
    elif h1 is None:
        return h2
    elif h2 is None:
        return h1
    
    if h1.data <= h2.data:
        head = h1
        cur1 = h1
        cur2 = h2
    else:
        head = h2
        cur1 = h2
        cur2 = h1
    

    while cur1.next is not None and cur2 is not None:
        if cur1.data <= cur2.data and cur1.next.data > cur2.data:
            fwd = cur2.next
            cur2.next = cur1.next
            cur1.next = cur2

            cur2 = fwd
        cur1 = cur1.next
    
    if cur1.next is None:
        cur1.next = cur2

    return head
    


# def mergeSort(head, tail, len):
#     mid = len//2

#     if len == 1:
#         return head

#     if len == 2:
#         midPtr = head
#     elif len > 2:
#         midPtr = head
#         i= 0
#         while i < mid:
#             midPtr = midPtr.next
#             i += 1

#     head2 = midPtr.next
#     midPtr.next = None
#     left = mergeSort(head, midPtr, mid+1)

#     right = mergeSort(head2, tail, len - mid)

#     return mergeSorted(left, right)

def mergeSort(head):
    if head is None or head.next is None:
        return head

    # Find the middle using slow/fast pointer
    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Split the list into two halves
    prev.next = None  # Break the link

    # Sort both halves
    left = mergeSort(head)
    right = mergeSort(slow)

    # Merge sorted halves
    return mergeSorted(left, right)

a = LinkedList()
a.insertAtTail(1)
a.insertAtTail(4)
a.insertAtTail(6)
a.insertAtTail(1)
a.insertAtTail(2)
a.printList()

new = mergeSort(a.head, a.tail, 5)

printll(new)




