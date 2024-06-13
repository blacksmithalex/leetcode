from math import gcd
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        freq = {}
        for num in deck:
            freq[num] = freq.get(num, 0) + 1
        G = gcd(*freq.values())
        if G != 1:
            for num in freq:
                freq[num] = freq[num] % G
        return len(set(freq.values())) == 1