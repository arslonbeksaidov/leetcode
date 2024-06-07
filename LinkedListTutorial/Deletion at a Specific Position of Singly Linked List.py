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

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def removeAtPosition(self, position):
        if position == 0:
            temp = self.head
            self.head = self.head.next
            del temp
            return
        current = self.head
        for i in range(1, position):
            if not current.next:
                return None
            current = current.next
        if current.next is None:
            print("Position is beyond the end of the list. Cannot delete.")
        else:
            temp = current.next
            current.next = current.next.next
            del temp


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)
    llist.push(5)
    llist.removeAtPosition(4)
    llist.print_linked_list()
