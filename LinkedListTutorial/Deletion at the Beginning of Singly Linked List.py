class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def push(head, data):
    if not head:
        return Node(data)
    newData = Node(data)
    newData.next = head
    head = newData
    return head



def removeAtFirstNode(head):
    if not head:
        return None
    temp = head
    head = head.next
    temp = None
    return head


def print_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next


if __name__ == "__main__":
    head = None
    head = push(head=head, data=1)
    head = push(head=head, data=2)
    head = push(head=head, data=3)
    head = push(head=head, data=4)
    head = removeAtFirstNode(head)
    print_list(head=head)
