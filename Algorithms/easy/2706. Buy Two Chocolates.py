class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        m1, m2 = 100, 100
        for p in prices:
            if p < m1:
                m2 = m1
                m1 = p
            elif p < m2:
                m2 = p
        if money >= m1 + m2:
            return money - (m1 + m2)
        else:
            return money