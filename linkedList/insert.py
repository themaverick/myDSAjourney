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

a = LinkedList()
a.insertAtHead(6)
a.insertAtHead(7)
a.insertAtHead(10)
a.insertAtTail(5)
a.insertAtPos(11, 1)
a.deletePos(2)

a.printList()

