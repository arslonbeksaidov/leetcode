class Node:
    def __init__(self):
        self.data = None
        self.next = None


def insertAtBeginning(head, new_data):
    new_node = Node()
    new_node.next = head
    new_node.data = new_data
    head = new_node
    return head


def print_list(head):
    while head:
        print(head.data)
        head = head.next


if __name__ == '__main__':
    head = None
    head = insertAtBeginning(head, 1)
    head = insertAtBeginning(head, 2)
    head = insertAtBeginning(head, 3)
    head = insertAtBeginning(head, 4)
    print_list(head)
