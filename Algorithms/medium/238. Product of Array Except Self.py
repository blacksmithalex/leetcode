# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curnode = head
        while (curnode and curnode.next):
            if (curnode.next.val == curnode.val):
                curnode.next = curnode.next.next
                continue
            curnode = curnode.next
        return head