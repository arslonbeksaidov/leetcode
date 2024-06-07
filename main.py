if __name__ == '__main__':
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def traverse_linked_list(head):
        current = head
        while current is not None:
            current = current.next


    def search_linked_list(head, target):
        current = head
        while current is not None:
            if current.data == target:
                return current.data
            current = current.next

    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.next = third

    traverse_linked_list(head)
    search_linked_list(head,1)
