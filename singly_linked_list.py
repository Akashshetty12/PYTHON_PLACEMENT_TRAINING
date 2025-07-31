class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addData(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new

    def display(self):
        current = self.head
        if current is None:
            print("Linked List is empty")
            return
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def delete(self,a):
        if self.head == None:
            print("Linked List is empty")
        elif a == 1:
            temp = self.head
            self.head = temp.next
        else:
            prev = None
            current = self.head
            for i in range(1,a):
                prev = current
                current = current.next
            prev.next = current.next

l = LinkedList()
l.addData(20)
l.addData(30)
l.addData(40)
l.addData(50)
l.display()
l.delete(1)
l.delete(3)
l.display()
