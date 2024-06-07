class Solution(object):

    class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def mergeTwoLists(self, list1, list2):
        list = []
        while list1 is not None:
            list.append(list1.val)
            list1 = list1.next

        while list2 is not None:
            list.append(list2.val)
            list2 = list2.next
        current = self.ListNode(list[0])

        for x in list[1:]:
            current.next = self.ListNode(x)
            current = current.next
        return current








ans = Solution().mergeTwoLists([1, 2, 3], [1, 2, 3, 5])
