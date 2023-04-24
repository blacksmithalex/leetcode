class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for l in s:
            if len(stack) != 0:
                l1 = stack[-1] == '(' and l == ')'
                l2 = stack[-1] == '{' and l == '}'
                l3 = stack[-1] == '[' and l == ']'
                if l1 or l2 or l3:
                    stack.pop()
                else:
                    stack.append(l)
            else:
                stack.append(l)
        return len(stack) == 0 