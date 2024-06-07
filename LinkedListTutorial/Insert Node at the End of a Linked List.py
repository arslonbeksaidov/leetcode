class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def append(self, data):
        newNode = Node(data)
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def print_llist(self):
        while self.head:
            print(self.head.data)
            self.head = self.head.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.append(9)
    llist.print_llist()
