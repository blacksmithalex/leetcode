class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        key = key.replace(' ', '')
        keycopy = ''
        for i in range(len(key)):
            if key.count(key[i], 0, i) == 0:
                keycopy += key[i]
        key = keycopy

        letters = []
        for i in range(97, 123):
            letters.append(chr(i))

        subs = {}
        for i in range(len(key)):
            subs[key[i]] = letters[i]
        subs[' '] = ' '

        res = ''.join([subs[x] for x in message])
        return res