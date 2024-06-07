class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def print_llist(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insertAtPosition(self, value, position):
        newNode = Node(value)
        if position == 0 or self.head is None:
            newNode.next = self.head
            self.head = newNode

        current = self.head
        for i in range(1, position):
            if current.next is None:
                break
            current = current.next
        newNode.next = current.next
        current.next = newNode


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(6)
    llist.push(7)
    llist.push(8)
    llist.push(9)
    llist.insertAtPosition(100,4)
    llist.print_llist()
