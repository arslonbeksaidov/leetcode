class Solution(object):
    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def mergeTwoLists(self, list1, list2):
        list = []
        while list1 or list2:
            if list1:
                list.append(list1.val)
                list1 = list1.next
            if list2:
                list.append(list2.val)
                list2 = list2.next
        list = reversed(sorted(list))
        head = None
        for x in list:
            newNode = self.ListNode(x)
            newNode.next = head
            head = newNode
        return head


solution = Solution()
one = solution.ListNode(1)
two = solution.ListNode(0)
three = solution.ListNode(3)
one.next = two
two.next = three
solution.mergeTwoLists(one, two)
