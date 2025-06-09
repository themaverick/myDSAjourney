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

# def rmDuplicateSorted(ll):
#     temp = ll.head
#     a = ll.head.data

#     while temp is not None and temp.next is not None:
#         if temp.next.data == a:
#             temp2 = temp.next
#             while temp2.data == a and temp2.next is not None:
#                 temp2 = temp2.next
#             if temp2.next is None:
#                 temp.next = None
#                 ll.tail = temp
#             else:
#                 temp.next = temp2
#                 temp = temp.next
#             a = temp.data
#         else:
#             temp = temp.next
#             a = temp.data
#     return

def rmDuplicateSorted(ll):
    cur = ll.head

    while cur is not None:
        if cur.next is not None and cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return

a = LinkedList()
# a.insertAtTail(3)
# a.insertAtTail(3)
# a.insertAtTail(4)
# a.insertAtTail(6)
# a.insertAtTail(6)
# a.insertAtTail(6)
# a.insertAtTail(7)
# a.insertAtTail(9)
# a.insertAtTail(11)
# a.insertAtTail(12)
# a.insertAtTail(12)
a.insertAtTail(1)
a.insertAtTail(1)
a.insertAtTail(1)
a.insertAtTail(2)
a.insertAtTail(3)
a.printList()
rmDuplicateSorted(a)
a.printList()



