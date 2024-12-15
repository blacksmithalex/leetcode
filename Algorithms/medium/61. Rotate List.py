# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        last_element = head
        length = 1
        while last_element.next:
            last_element = last_element.next
            length += 1
        k = k % length

        last_element.next = head
        cur_node = head
        for _ in range(length - k - 1):
            cur_node = cur_node.next
        head = cur_node.next
        cur_node.next = None
        return head

