class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.data == data:
                    current.next = current.next.next
                    break
                current = current.next

    def length(self):
        if not self.head:
            return 0
        current = self.head
        count = 1
        while current.next:
            current = current.next
            count += 1
        return count
sll = SinglyLinkedList()
sll.insert(1)
sll.insert(2)
sll.insert(3)
print(sll.display())  # [1, 2, 3]
print(sll.length())   # 3
sll.delete(2)
print(sll.display())  # [1, 3]
print(sll.length())   # 2