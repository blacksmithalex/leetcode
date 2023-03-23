class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        digits.append(0)
        a = 1
        for i in range(len(digits)):
            a, b = (digits[i] + 1) // 10, (digits[i] + 1) % 10
            digits[i] = b
            if a == 0:
                break
        if digits[-1] == 0:
            digits.pop()
        return digits[::-1]

'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join([str(x) for x in digits])) + 1
        return [int(x) for x in str(num)]

'''