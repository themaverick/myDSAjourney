class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtHead(self, data):
        temp = Node(data)
        temp.next =self.head
        self.head = temp
        return

    def insertAtTail(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            return
        temp2 = self.head
        while temp2.next is not None:
            temp2 = temp2.next
        temp2.next = temp
        return

    def insertAtPos(self, data, pos):
        if pos == 1:
            self.insertAtHead(data)
            return
        temp = Node(data)
        temp2 = self.head
        if pos >= 2:
            for i in range(pos-2):
                temp2 = temp2.next
        temp.next = temp2.next
        temp2.next = temp
        return

    def deletePos(self, pos):
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(pos-2):
            temp = temp.next
        temp.next = temp.next.next

    def printList(self):
        temp = self.head
        while(temp != None):
            print(f"{temp.data}", end=" -> " if temp.next else "")
            temp = temp.next
        return

    # def reverse(self):
    #     if self.head.next == None:
    #         return
    #     if self.head.next.next == None:
    #         temp = self.head
    #         temp.next.next = self.head
    #         self.head = temp.next
    #         temp.next = None
    #         return

    #     temp1 = self.head
    #     temp2 = self.head.next
    #     temp3 = self.head.next.next

    #     temp1.next = None
    #     while temp3 != None:
    #         temp2.next = temp1
    #         temp1 = temp2
    #         temp2 = temp3
    #         temp3 = temp3.next
    #     temp2.next = temp1
    #     self.head = temp2
    #     return

    def reverse(self):
        prev = None
        cur = self.head

        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev
        return

    def recursiveReverse(self, prev=None, cur=None, _first_call=True):

        if _first_call:
            cur = self.head

        if cur is None:
            self.head = prev
            return
        
        fwd = cur.next
        cur.next = prev
        self.recursiveReverse(cur, fwd,_first_call=False)

a = LinkedList()
a.insertAtHead(6)
a.insertAtHead(7)
a.insertAtHead(10)
a.insertAtTail(5)
a.insertAtPos(11, 1)
a.printList()
a.recursiveReverse()
print()
a.printList()


