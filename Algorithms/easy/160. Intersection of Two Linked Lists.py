# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA, pB = headA, headB
        while pA != pB:
            if not pA:
                pA = headB
            else:
                pA = pA.next
            if not pB:
                pB = headA
            else:
                pB = pB.next
        return pA

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def get_nodes(head):
            nodes = []
            while head:
                nodes.append(head)
                head = head.next
            return nodes
        
        nodesA = get_nodes(headA)
        nodesB = get_nodes(headB)

        ind = -1
        min_len = min(len(nodesA), len(nodesB))
        while abs(ind) <= min_len and  nodesA[ind] == nodesB[ind]:
            ind -= 1
        if ind == -1 and nodesA[ind] != nodesB[ind]:
            return None
        return nodesA[ind + 1]

        