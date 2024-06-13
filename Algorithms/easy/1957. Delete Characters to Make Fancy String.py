class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for l in s:
            if len(stack) > 1 and l == stack[-1] == stack[-2]:
                stack.pop()
            stack.append(l)
        return ''.join(stack)