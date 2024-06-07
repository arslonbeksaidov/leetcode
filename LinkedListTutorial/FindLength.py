class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, newNode):
        newNode = Node(newNode)
        newNode.next = self.head
        self.head = newNode

    def fineLengthLinkedList(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)

    print(llist.fineLengthLinkedList())