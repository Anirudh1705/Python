class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def display(self):
        elements = []
        current = self.head
        if not self.head:
            return elements
        while True:
            elements.append(current.data)
            current = current.next
            if current == self.head:
                break
        return elements

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
        current = self.head
        while current.next != self.head:
            if current.next.data == data:
                current.next = current.next.next
                break
            current = current.next

    def length(self):
        if not self.head:
            return 0
        current = self.head
        count = 1
        while current.next != self.head:
            current = current.next
            count += 1
        return count
cll = CircularLinkedList()
cll.insert(1)
cll.insert(2)
cll.insert(3)
print(cll.display())  # [1, 2, 3]
print(cll.length())   # 3
cll.delete(2)
print(cll.display())  # [1, 3]
print(cll.length())   # 2