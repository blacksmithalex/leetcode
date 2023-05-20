class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        uniq = set()
        for email in emails:
            part1, part2 = email.split('@')
            part1 = part1.replace('.', '')
            if '+' in part1:
                ind_plus = part1.find('+')
                part1 = part1[:ind_plus]
            uniq.add(part1 + '@' + part2)
        return len(uniq)