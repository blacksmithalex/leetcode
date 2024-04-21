class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        numdays = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        Alice_month_1, Alice_day_1 = [int(x) for x in arriveAlice.split('-')]
        Alice_month_2, Alice_day_2 = [int(x) for x in leaveAlice.split('-')]
        Bob_month_1, Bob_day_1 = [int(x) for x in arriveBob.split('-')]
        Bob_month_2, Bob_day_2 = [int(x) for x in leaveBob.split('-')]
        Alicestart = Aliceend = Bobstart = Bobend = 0
        for i in range(1, Alice_month_1):
            Alicestart += numdays[i]
        Alicestart += Alice_day_1
        for i in range(1, Alice_month_2):
            Aliceend += numdays[i]
        Aliceend += Alice_day_2

        for i in range(1, Bob_month_1):
            Bobstart += numdays[i]
        Bobstart += Bob_day_1
        for i in range(1, Bob_month_2):
            Bobend += numdays[i]
        Bobend += Bob_day_2

        return len(set(range(Bobstart, Bobend + 1)) & set(range(Alicestart, Aliceend + 1)))



