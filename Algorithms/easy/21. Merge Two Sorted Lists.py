# Version 1
# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         if not list1:
#             return list2
#         if not list2:
#             return list1
#         if (list1.val < list2.val):
#             list1.next = self.mergeTwoLists(list1.next, list2)
#             return list1
#         else:
#             list2.next = self.mergeTwoLists(list1, list2.next)
#             return list2

#Version 2

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        res = ListNode()
        if list1.val < list2.val:
            res.val = list1.val
            list1 = list1.next
        else:
            res.val = list2.val
            list2 = list2.next
        cur = res
        while list1 and list2:
            cur.next = ListNode()
            cur = cur.next
            if list1.val < list2.val:
                cur.val = list1.val
                list1 = list1.next
            else:
                cur.val = list2.val
                list2 = list2.next
        while list1:
            cur.next = ListNode()
            cur = cur.next
            cur.val = list1.val
            list1 = list1.next
        while list2:
            cur.next = ListNode()
            cur = cur.next
            cur.val = list2.val
            list2 = list2.next
        return res