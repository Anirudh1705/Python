class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
    def size(self):
        return len(self.items)

def reverse_string(input_string):
    """Function to reverse a string using a stack."""
    stack = Stack()
    # Push each character onto the stack
    for char in input_string:
        stack.push(char)
    # Pop each character from the stack to get reversed order
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

def main():
    """Main function to accept user input and reverse the string."""
    input_string = "Educative"
    print("Reversed string:", reverse_string(input_string))

if __name__ == "__main__":
    main()