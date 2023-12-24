class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: intй
        """
        people = sorted(people)
        num_of_boats = 0
        l, r = 0, len(people) - 1
        while l < r:
            if people[l] + people[r] <= limit:
                num_of_boats += 1
                l += 1
                r -= 1
            else:
                num_of_boats += 1
                r -= 1
        if l == r:
            num_of_boats += 1
        return num_of_boats