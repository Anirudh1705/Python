class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def size(self):
        return len(self.items)


def main():
    """Main function to demonstrate the queue operations."""
    q = Queue()

    print("Is queue empty:", q.is_empty())
    print("Enqueue elements: 1 2 3 4 5")
    for i in range(1, 6):
        q.enqueue(i)
    print("Size of queue:", q.size())
    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())
    print("Size of queue:", q.size())
    print("Queue:", q.items)


if __name__ == "__main__":
    main()