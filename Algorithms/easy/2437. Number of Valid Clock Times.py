class Solution:
    def countTime(self, time: str) -> int:
        h1 = range(3) if time[0] == '?' else [int(time[0])]
        h2 = range(10) if time[1] == '?' else [int(time[1])]
        m1 = range(6) if time[3] == '?' else [int(time[3])]
        m2 = range(10) if time[4] == '?' else [int(time[4])]
        total = 0
        for h in h1:
            for hh in h2:
                for m in m1:
                    for mm in m2:
                        if f"{h}{hh}:{m}{mm}" <= "23:59":
                            total += 1
        return total