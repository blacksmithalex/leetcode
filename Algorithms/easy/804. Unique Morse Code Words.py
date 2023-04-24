class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = [chr(i) for i in range(97, 123)]
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse = {}
        for i in range(len(letters)):
            morse[letters[i]] = codes[i]
        all_words = set()
        for w in words:
            new_w = ''.join([morse[x] for x in w])
            all_words.add(new_w)
        return len(all_words)

