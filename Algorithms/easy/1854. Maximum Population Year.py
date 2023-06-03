class Solution(object):
    def maximumPopulation(self, logs):
        """
        :type logs: List[List[int]]
        :rtype: int
        """
        num_b, num_d = {}, {}
        for year in range(1950, 2050 + 1):
            num_b[year], num_d[year] = 0, 0
        for birth, death in logs:
            num_b[birth] += 1
            num_d[death] += 1
        count, mcount, myear = 0, 0, 0
        for year in range(1950, 2050 + 1):
            count += num_b[year] - num_d[year]
            if count > mcount:
                mcount = count
                myear = year
        return myear

